"""Database update2

Revision ID: 330d1ace2d52
Revises: 20d6c1056560
Create Date: 2024-01-08 21:36:12.354045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '330d1ace2d52'
down_revision: Union[str, None] = '20d6c1056560'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pereval_added', 'status',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.Text(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pereval_added', 'status',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=10),
               nullable=True)
    # ### end Alembic commands ###