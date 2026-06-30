"""initial_schema

Revision ID: 938c929947df
Revises: 
Create Date: 2026-06-30 02:28:01.038101

"""
from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = '938c929947df'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
