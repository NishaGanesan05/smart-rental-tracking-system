from datetime import datetime

from sqlalchemy.orm import Session

from app.models import Alert, Asset, Recommendation, Rental, Telemetry


def generate_recommendations(db: Session):
    assets = db.query(Asset).all()
    recommendations_created = []

    for asset in assets:

        # Get the latest telemetry
        telemetry = (
            db.query(Telemetry)
            .filter(Telemetry.asset_id == asset.asset_id)
            .order_by(Telemetry.recorded_at.desc())
            .first()
        )

        if not telemetry:
            continue

        # Get open alerts
        open_alerts = (
            db.query(Alert)
            .filter(
                Alert.asset_id == asset.asset_id,
                Alert.status == "OPEN"
            )
            .all()
        )

        # Get current rental
        rental = (
            db.query(Rental)
            .filter(
                Rental.asset_id == asset.asset_id,
                Rental.status.in_(["ACTIVE", "OVERDUE"])
            )
            .first()
        )
        # --------------------------------------------------
        # HIGH IDLE → UTILIZATION RECOMMENDATION
        # --------------------------------------------------

        high_idle_alert = next(
            (
                alert
                for alert in open_alerts
                if alert.alert_type == "HIGH_IDLE"
            ),
            None
        )

        # Only recommend utilization action when the asset
        # is actually being rented/operated.
        if high_idle_alert and rental:

            existing = (
                db.query(Recommendation)
                .filter(
                    Recommendation.asset_id == asset.asset_id,
                    Recommendation.recommendation_type == "UTILIZATION",
                    Recommendation.status == "OPEN"
                )
                .first()
            )

            if not existing:

                recommendation = Recommendation(
                    asset_id=asset.asset_id,
                    recommendation_type="UTILIZATION",
                    priority="HIGH",
                    message=(
                        f"Review utilization of {asset.asset_id} "
                        f"and consider reallocating the asset."
                    ),
                    reason=(
                        "The rented asset has significantly higher "
                        "idle time than runtime."
                    ),
                    status="OPEN",
                    created_at=datetime.utcnow()
                )

                db.add(recommendation)
                recommendations_created.append(recommendation)

        # --------------------------------------------------
        # HEAVY USAGE → MAINTENANCE RECOMMENDATION
        # --------------------------------------------------

        heavy_usage_alert = next(
            (
                alert
                for alert in open_alerts
                if alert.alert_type == "HEAVY_USAGE"
            ),
            None
        )

        if heavy_usage_alert:

            existing = (
                db.query(Recommendation)
                .filter(
                    Recommendation.asset_id == asset.asset_id,
                    Recommendation.recommendation_type == "MAINTENANCE",
                    Recommendation.status == "OPEN"
                )
                .first()
            )

            if not existing:

                recommendation = Recommendation(
                    asset_id=asset.asset_id,
                    recommendation_type="MAINTENANCE",
                    priority="MEDIUM",
                    message=(
                        f"Schedule a maintenance inspection for "
                        f"{asset.asset_id}."
                    ),
                    reason=(
                        "The asset is showing unusually high "
                        "operating usage."
                    ),
                    status="OPEN",
                    created_at=datetime.utcnow()
                )

                db.add(recommendation)
                recommendations_created.append(recommendation)

        # --------------------------------------------------
        # OVERDUE RENTAL → RENTAL FOLLOW-UP
        # --------------------------------------------------

        if rental and rental.status == "OVERDUE":

            existing = (
                db.query(Recommendation)
                .filter(
                    Recommendation.asset_id == asset.asset_id,
                    Recommendation.recommendation_type == "RENTAL_FOLLOWUP",
                    Recommendation.status == "OPEN"
                )
                .first()
            )

            if not existing:

                recommendation = Recommendation(
                    asset_id=asset.asset_id,
                    recommendation_type="RENTAL_FOLLOWUP",
                    priority="HIGH",
                    message=(
                        f"Follow up with the customer regarding "
                        f"the overdue rental of {asset.asset_id}."
                    ),
                    reason=(
                        "The rental return date has passed and "
                        "the asset is still marked as rented."
                    ),
                    status="OPEN",
                    created_at=datetime.utcnow()
                )

                db.add(recommendation)
                recommendations_created.append(recommendation)

    db.commit()

    return recommendations_created