"""empty message

Revision ID: f7ae5552bcde
Revises: 
Create Date: 2022-01-04 15:29:53.636552

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f7ae5552bcde'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_role',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.drop_table('article')
    op.drop_index('phone', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=15), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('phone', mysql.VARCHAR(length=11), nullable=True),
    sa.Column('isdelete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('phone', 'user', ['phone'], unique=False)
    op.create_table('article',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('click_num', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('save_num', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('love_num', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='article_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.drop_table('user_role')
    # ### end Alembic commands ###
