"""create tables

Revision ID: 863b548fcaf1
Revises: 
Create Date: 2020-08-14 22:45:49.840081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '863b548fcaf1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('interests_users', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('interests_users', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.alter_column('interests_users', 'interests_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('interests_users', 'users_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('interests_users', 'users_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('interests_users', 'interests_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('interests_users', 'updated_at')
    op.drop_column('interests_users', 'id')
    # ### end Alembic commands ###