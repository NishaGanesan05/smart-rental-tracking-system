from fastapi import FastAPI
from sqlalchemy import text

from app.database import Base, engine
from app.models import Asset, Operator, Site

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Smart Rental Tracking System",
    description="AI-powered rental asset control tower",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Smart Rental Tracking System API is running"
    }


@app.get("/health/database")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "connection failed",
            "error": str(e)
        }