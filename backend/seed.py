from app.database import SessionLocal
from app.models import Asset, Operator, Site


def seed_database():
    db = SessionLocal()

    try:
        # -------------------------
        # SITES
        # -------------------------
        sites = [
            Site(
                site_id="S001",
                site_name="Project Site 001",
                location="Bangalore",
                latitude=12.9716,
                longitude=77.5946,
            ),
            Site(
                site_id="S002",
                site_name="Project Site 002",
                location="Chennai",
                latitude=13.0827,
                longitude=80.2707,
            ),
            Site(
                site_id="S003",
                site_name="Project Site 003",
                location="Hyderabad",
                latitude=17.3850,
                longitude=78.4867,
            ),
            Site(
                site_id="S004",
                site_name="Project Site 004",
                location="Mumbai",
                latitude=19.0760,
                longitude=72.8777,
            ),
            Site(
                site_id="S005",
                site_name="Project Site 005",
                location="Pune",
                latitude=18.5204,
                longitude=73.8567,
            ),
            Site(
                site_id="S006",
                site_name="Project Site 006",
                location="Delhi",
                latitude=28.6139,
                longitude=77.2090,
            ),
        ]

        # -------------------------
        # ASSETS
        # -------------------------
        assets = [
            Asset(
                asset_id="EQX1001",
                asset_type="Excavator",
                model="CAT-320",
                serial_number="CAT320-1001",
                status="ACTIVE",
                site_id="S001",
            ),
            Asset(
                asset_id="EQX1002",
                asset_type="Crane",
                model="CAT-250",
                serial_number="CAT250-1002",
                status="UNASSIGNED",
                site_id=None,
            ),
            Asset(
                asset_id="EQX1003",
                asset_type="Bulldozer",
                model="CAT-D6",
                serial_number="CATD6-1003",
                status="ACTIVE",
                site_id="S002",
            ),
            Asset(
                asset_id="EQX1004",
                asset_type="Loader",
                model="CAT-950",
                serial_number="CAT950-1004",
                status="ACTIVE",
                site_id="S004",
            ),
            Asset(
                asset_id="EQX1005",
                asset_type="Bulldozer",
                model="CAT-D6",
                serial_number="CATD6-1005",
                status="ACTIVE",
                site_id="S006",
            ),
            Asset(
                asset_id="EQX1006",
                asset_type="Excavator",
                model="CAT-320",
                serial_number="CAT320-1006",
                status="ACTIVE",
                site_id="S005",
            ),
            Asset(
                asset_id="EQX1007",
                asset_type="Excavator",
                model="CAT-320",
                serial_number="CAT320-1007",
                status="UNASSIGNED",
                site_id=None,
            ),
        ]

        # -------------------------
        # OPERATORS
        # -------------------------
        operators = [
            Operator(
                operator_id="OP301",
                name="Operator 301",
                contact="9000000301",
                status="ACTIVE",
                site_id="S006",
            ),
            Operator(
                operator_id="OP302",
                name="Operator 302",
                contact="9000000302",
                status="ACTIVE",
                site_id="S002",
            ),
            Operator(
                operator_id="OP303",
                name="Operator 303",
                contact="9000000303",
                status="ACTIVE",
                site_id="S004",
            ),
            Operator(
                operator_id="OP304",
                name="Operator 304",
                contact="9000000304",
                status="ACTIVE",
                site_id="S001",
            ),
        ]

        # -------------------------
        # INSERT ONLY IF NOT EXISTS
        # -------------------------

        for site in sites:
            existing = db.get(Site, site.site_id)

            if not existing:
                db.add(site)

        for asset in assets:
            existing = db.get(Asset, asset.asset_id)

            if not existing:
                db.add(asset)

        for operator in operators:
            existing = db.get(Operator, operator.operator_id)

            if not existing:
                db.add(operator)

        db.commit()

        print("Database seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()