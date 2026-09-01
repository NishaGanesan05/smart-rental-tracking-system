from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.routes.rentals import router as rental_router
from app.routes.assets import router as asset_router
from app.routes.kpis import router as kpi_router
from app.routes.telemetry import router as telemetry_router
from app.routes.alerts import router as alert_router
from app.routes.recommendations import router as recommendation_router
from app.routes.ml_anomalies import router as ml_anomaly_router



app = FastAPI(
    title="Smart Rental Tracking System",
    description="AI-powered rental asset control tower",
    version="1.0.0"
)


app.include_router(rental_router)
app.include_router(asset_router)
app.include_router(kpi_router)
app.include_router(telemetry_router)
app.include_router(alert_router)
app.include_router(recommendation_router)
app.include_router(ml_anomaly_router)



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
