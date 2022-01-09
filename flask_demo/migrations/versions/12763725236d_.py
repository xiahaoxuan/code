"""empty message

Revision ID: 12763725236d
Revises: 54172695f37f
Create Date: 2022-01-07 23:27:02.730144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12763725236d'
down_revision = '54172695f37f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('icon', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'icon')
    # ### end Alembic commands ###