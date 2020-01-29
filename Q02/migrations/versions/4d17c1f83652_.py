"""empty message

Revision ID: 4d17c1f83652
Revises: 088af044833b
Create Date: 2020-01-27 22:13:50.517712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d17c1f83652'
down_revision = '088af044833b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_model', sa.Column('extension', sa.BigInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users_model', 'extension')
    # ### end Alembic commands ###
