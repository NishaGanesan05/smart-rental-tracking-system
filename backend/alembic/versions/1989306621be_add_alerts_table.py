"""add alerts table

Revision ID: 1989306621be
Revises: a1c4c013e1bf
Create Date: 2026-09-01 23:45:04.456422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1989306621be"
down_revision: Union[str, Sequence[str], None] = "a1c4c013e1bf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "alerts",
        sa.Column(
            "alert_id",
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
            "alert_type",
            sa.String(length=50),
            nullable=False
        ),
        sa.Column(
            "severity",
            sa.String(length=20),
            nullable=False
        ),
        sa.Column(
            "message",
            sa.Text(),
            nullable=False
        ),
        sa.Column(
            "detected_at",
            sa.DateTime(),
            nullable=False
        ),
        sa.Column(
            "status",
            sa.String(length=20),
            nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["asset_id"],
            ["assets.asset_id"]
        ),
        sa.PrimaryKeyConstraint("alert_id")
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("alerts")