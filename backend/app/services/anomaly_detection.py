from datetime import datetime

from sqlalchemy.orm import Session

from app.models import Alert, Asset, Telemetry


def detect_anomalies(db: Session):
    assets = db.query(Asset).all()

    alerts_created = []

    for asset in assets:

        # Get latest telemetry reading
        telemetry = (
            db.query(Telemetry)
            .filter(Telemetry.asset_id == asset.asset_id)
            .order_by(Telemetry.recorded_at.desc())
            .first()
        )

        if not telemetry:
            continue

        # -------------------------
        # HIGH IDLE DETECTION
        # -------------------------
        if (
            telemetry.runtime_hours is not None
            and telemetry.idle_hours is not None
            and telemetry.runtime_hours > 0
            and telemetry.idle_hours > telemetry.runtime_hours * 2
        ):
            existing_alert = (
                db.query(Alert)
                .filter(
                    Alert.asset_id == asset.asset_id,
                    Alert.alert_type == "HIGH_IDLE",
                    Alert.status == "OPEN"
                )
                .first()
            )

            if not existing_alert:
                alert = Alert(
                    asset_id=asset.asset_id,
                    alert_type="HIGH_IDLE",
                    severity="HIGH",
                    message=(
                        f"Asset {asset.asset_id} has unusually high "
                        f"idle time compared with runtime."
                    ),
                    detected_at=datetime.utcnow(),
                    status="OPEN"
                )

                db.add(alert)
                alerts_created.append(alert)

        # -------------------------
        # LOW FUEL DETECTION
        # -------------------------
        if (
            telemetry.fuel_level is not None
            and telemetry.fuel_level < 20
        ):
            existing_alert = (
                db.query(Alert)
                .filter(
                    Alert.asset_id == asset.asset_id,
                    Alert.alert_type == "LOW_FUEL",
                    Alert.status == "OPEN"
                )
                .first()
            )

            if not existing_alert:
                alert = Alert(
                    asset_id=asset.asset_id,
                    alert_type="LOW_FUEL",
                    severity="MEDIUM",
                    message=(
                        f"Asset {asset.asset_id} has low fuel "
                        f"level ({telemetry.fuel_level}%)."
                    ),
                    detected_at=datetime.utcnow(),
                    status="OPEN"
                )

                db.add(alert)
                alerts_created.append(alert)

        # -------------------------
        # HEAVY USAGE DETECTION
        # -------------------------
        if (
            telemetry.runtime_hours is not None
            and telemetry.runtime_hours > 1.0
        ):
            existing_alert = (
                db.query(Alert)
                .filter(
                    Alert.asset_id == asset.asset_id,
                    Alert.alert_type == "HEAVY_USAGE",
                    Alert.status == "OPEN"
                )
                .first()
            )

            if not existing_alert:
                alert = Alert(
                    asset_id=asset.asset_id,
                    alert_type="HEAVY_USAGE",
                    severity="MEDIUM",
                    message=(
                        f"Asset {asset.asset_id} is experiencing "
                        f"heavy operating usage."
                    ),
                    detected_at=datetime.utcnow(),
                    status="OPEN"
                )

                db.add(alert)
                alerts_created.append(alert)

    db.commit()

    return alerts_created
