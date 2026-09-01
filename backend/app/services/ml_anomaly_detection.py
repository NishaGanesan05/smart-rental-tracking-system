import numpy as np
from sqlalchemy.orm import Session
from sklearn.ensemble import IsolationForest

from app.models import Telemetry


def detect_ml_anomalies(db: Session):
    telemetry_records = (
        db.query(Telemetry)
        .order_by(Telemetry.recorded_at)
        .all()
    )

    if len(telemetry_records) < 10:
        return []

    features = []

    for record in telemetry_records:
        runtime = record.runtime_hours or 0
        idle = record.idle_hours or 0
        fuel = record.fuel_level or 0
        speed = record.speed or 0

        idle_runtime_ratio = (
            idle / runtime if runtime > 0 else idle
        )

        features.append([
            runtime,
            idle,
            fuel,
            speed,
            idle_runtime_ratio
        ])

    X = np.array(features)

    model = IsolationForest(
        n_estimators=100,
        contamination=0.15,
        random_state=42
    )

    predictions = model.fit_predict(X)
    scores = model.decision_function(X)

    results = []

    for record, prediction, score in zip(
        telemetry_records,
        predictions,
        scores
    ):
        is_anomaly = prediction == -1

        # Convert the raw ML score into a simple
        # business-friendly category.
        if not is_anomaly:
            anomaly_status = "NORMAL"
        elif score < -0.05:
            anomaly_status = "HIGH"
        else:
            anomaly_status = "MEDIUM"

        results.append({
            "telemetry_id": record.telemetry_id,
            "asset_id": record.asset_id,
            "is_anomaly": is_anomaly,
            "anomaly_score": round(float(score), 4),
            "anomaly_status": anomaly_status,
            "runtime_hours": record.runtime_hours,
            "idle_hours": record.idle_hours,
            "fuel_level": record.fuel_level,
            "speed": record.speed
        })

    return results