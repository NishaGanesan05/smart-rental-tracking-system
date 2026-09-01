from datetime import date
from app.database import SessionLocal
from app.models import Asset, Operator, Site, Customer, Rental


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
        # CUSTOMERS
        # -------------------------
        customers = [
            Customer(
                customer_id="C001",
                customer_name="ABC Construction",
                company_name="ABC Construction Pvt Ltd",
                contact="9876500001",
                email="contact@abcconstruction.com",
                status="ACTIVE",
            ),
            Customer(
                customer_id="C002",
                customer_name="BuildRight Infrastructure",
                company_name="BuildRight Infrastructure Ltd",
                contact="9876500002",
                email="operations@buildright.com",
                status="ACTIVE",
            ),
            Customer(
                customer_id="C003",
                customer_name="Metro Earthworks",
                company_name="Metro Earthworks Pvt Ltd",
                contact="9876500003",
                email="admin@metroearthworks.com",
                status="ACTIVE",
            ),
            Customer(
                customer_id="C004",
                customer_name="GreenField Projects",
                company_name="GreenField Projects Pvt Ltd",
                contact="9876500004",
                email="projects@greenfield.com",
                status="ACTIVE",
            ),
            Customer(
                customer_id="C005",
                customer_name="Skyline Contractors",
                company_name="Skyline Contractors Ltd",
                contact="9876500005",
                email="fleet@skylinecontractors.com",
                status="ACTIVE",
            ),
        ]


        # -------------------------
        # RENTALS
        # -------------------------
        rentals = [
            Rental(
                rental_id="R001",
                customer_id="C001",
                asset_id="EQX1001",
                start_date="2026-08-28",
                expected_return_date="2026-09-07",
                actual_return_date=None,
                status="ACTIVE",
            ),
            Rental(
                rental_id="R002",
                customer_id="C002",
                asset_id="EQX1003",
                start_date="2026-08-20",
                expected_return_date="2026-08-30",
                actual_return_date=None,
                status="OVERDUE",
            ),
            Rental(
                rental_id="R003",
                customer_id="C003",
                asset_id="EQX1004",
                start_date="2026-08-25",
                expected_return_date="2026-09-05",
                actual_return_date=None,
                status="ACTIVE",
            ),
            Rental(
                rental_id="R004",
                customer_id="C004",
                asset_id="EQX1005",
                start_date="2026-08-10",
                expected_return_date="2026-08-20",
                actual_return_date="2026-08-19",
                status="RETURNED",
            ),
            Rental(
                rental_id="R005",
                customer_id="C005",
                asset_id="EQX1006",
                start_date="2026-08-30",
                expected_return_date="2026-09-08",
                actual_return_date=None,
                status="ACTIVE",
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

        for customer in customers:
            existing = db.get(Customer, customer.customer_id)

            if not existing:
                db.add(customer)

        for rental in rentals:
            existing = db.get(Rental, rental.rental_id)

            if not existing:
                db.add(rental)

        db.commit()

        print("Database seeded successfully.")


    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()