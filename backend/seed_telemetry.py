from datetime import datetime, timedelta

from app.database import SessionLocal
from app.models import Asset, Telemetry


def seed_telemetry():
    db = SessionLocal()

    try:
        assets = db.query(Asset).all()

        if not assets:
            print("No assets found.")
            return

        now = datetime.now()

        telemetry_data = []

        for asset in assets:
            # Generate 6 readings over the previous 6 hours
            for i in range(6):
                recorded_at = now - timedelta(hours=(5 - i))

                # Default realistic values
                runtime = 0.7
                idle = 0.3
                fuel = 75 - (i * 2)
                speed = 4.0

                # Create different usage patterns
                if asset.asset_id == "EQX1001":
                    # Normal excavator
                    runtime = 0.8
                    idle = 0.2
                    fuel = 80 - (i * 2)
                    speed = 3.5

                elif asset.asset_id == "EQX1002":
                    # Unassigned crane — mostly idle
                    runtime = 0.1
                    idle = 0.9
                    fuel = 65 - i
                    speed = 0.0

                elif asset.asset_id == "EQX1003":
                    # High-idle bulldozer
                    runtime = 0.3
                    idle = 1.5
                    fuel = 70 - (i * 4)
                    speed = 1.5

                elif asset.asset_id == "EQX1004":
                    # Normal loader
                    runtime = 0.9
                    idle = 0.2
                    fuel = 78 - (i * 2)
                    speed = 5.0

                elif asset.asset_id == "EQX1005":
                    # Heavy usage bulldozer
                    runtime = 1.2
                    idle = 0.3
                    fuel = 85 - (i * 5)
                    speed = 3.0

                elif asset.asset_id == "EQX1006":
                    # Normal excavator
                    runtime = 0.7
                    idle = 0.3
                    fuel = 72 - (i * 2)
                    speed = 3.0

                elif asset.asset_id == "EQX1007":
                    # Available excavator — not currently operating
                    runtime = 0.0
                    idle = 0.0
                    fuel = 90
                    speed = 0.0

                telemetry_data.append(
                    Telemetry(
                        asset_id=asset.asset_id,
                        recorded_at=recorded_at,
                        latitude=12.9716,
                        longitude=77.5946,
                        engine_hours=1000 + (i * runtime),
                        runtime_hours=runtime,
                        idle_hours=idle,
                        fuel_level=fuel,
                        speed=speed,
                    )
                )

        # Prevent duplicate seed data
        existing_count = db.query(Telemetry).count()

        if existing_count > 0:
            print(
                f"Telemetry table already contains "
                f"{existing_count} records. Skipping seed."
            )
            return

        db.add_all(telemetry_data)
        db.commit()

        print(
            f"Telemetry seeded successfully: "
            f"{len(telemetry_data)} records."
        )

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_telemetry()
