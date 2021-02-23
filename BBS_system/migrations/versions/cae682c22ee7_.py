"""empty message

Revision ID: cae682c22ee7
Revises: 8a2471d31478
Create Date: 2021-02-05 16:45:51.586328

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cae682c22ee7'
down_revision = '8a2471d31478'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('front_user', 'gender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('gender', mysql.ENUM('MALE', 'FEMALE', 'UNKNOW'), nullable=True))
    # ### end Alembic commands ###