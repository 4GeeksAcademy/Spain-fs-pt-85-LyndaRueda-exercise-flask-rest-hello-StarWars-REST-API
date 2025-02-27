"""empty message

Revision ID: 48457f664e85
Revises: c70f18df9203
Create Date: 2025-01-25 13:55:50.107552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48457f664e85'
down_revision = 'c70f18df9203'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_favorite',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('favorite_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['favorite_id'], ['favorites.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'favorite_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_favorite')
    # ### end Alembic commands ###
