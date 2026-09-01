"""add telemetry table

Revision ID: a1c4c013e1bf
Revises: dac44c4d01b1
Create Date: 2026-09-01 23:26:40.838363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a1c4c013e1bf"
down_revision: Union[str, Sequence[str], None] = "dac44c4d01b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "telemetry",
        sa.Column(
            "telemetry_id",
            sa.Integer(),
            autoincrement=True,
            nullable=False
        ),
        sa.Column(
            "asset_id",
            sa.String(length=20),
            nullable=False
        ),
        sa.Column(
            "recorded_at",
            sa.DateTime(),
            nullable=False
        ),
        sa.Column(
            "latitude",
            sa.Float(),
            nullable=True
        ),
        sa.Column(
            "longitude",
            sa.Float(),
            nullable=True
        ),
        sa.Column(
            "engine_hours",
            sa.Float(),
            nullable=True
        ),
        sa.Column(
            "runtime_hours",
            sa.Float(),
            nullable=True
        ),
        sa.Column(
            "idle_hours",
            sa.Float(),
            nullable=True
        ),
        sa.Column(
            "fuel_level",
            sa.Float(),
            nullable=True
        ),
        sa.Column(
            "speed",
            sa.Float(),
            nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["asset_id"],
            ["assets.asset_id"]
        ),
        sa.PrimaryKeyConstraint("telemetry_id")
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("telemetry")