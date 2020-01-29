"""empty message

Revision ID: 088af044833b
Revises: d6b6e58b9e69
Create Date: 2020-01-27 22:12:17.377974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '088af044833b'
down_revision = 'd6b6e58b9e69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_model', sa.Column('location', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users_model', 'location')
    # ### end Alembic commands ###