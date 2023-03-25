"""add name to User

Revision ID: 8a8fc7d83689
Revises: ae3f71631316
Create Date: 2023-03-23 19:48:41.106865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a8fc7d83689'
down_revision = 'ae3f71631316'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(length=128), nullable=True))
    op.create_unique_constraint(None, 'users', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'name')
    # ### end Alembic commands ###