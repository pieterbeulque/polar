"""Add User.is_admin

Revision ID: 2c68ca24df26
Revises: beaaa1a657d1
Create Date: 2025-07-23 13:31:58.348319

"""

import sqlalchemy as sa
from alembic import op

# Polar Custom Imports

# revision identifiers, used by Alembic.
revision = "2c68ca24df26"
down_revision = "beaaa1a657d1"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("is_admin", sa.Boolean(), nullable=True))
    op.execute("UPDATE users SET is_admin = FALSE WHERE is_admin IS NULL")
    op.alter_column("users", "is_admin", nullable=False, existing_type=sa.Boolean())

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_admin")
    # ### end Alembic commands ###
