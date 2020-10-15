"""empty message

Revision ID: 95af0c8c7f38
Revises: 4a9a410c11c7
Create Date: 2020-09-27 22:12:00.553514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95af0c8c7f38'
down_revision = '4a9a410c11c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('level', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'level')
    # ### end Alembic commands ###