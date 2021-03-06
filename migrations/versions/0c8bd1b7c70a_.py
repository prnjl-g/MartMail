"""empty message

Revision ID: 0c8bd1b7c70a
Revises: 9b52c8db3c9f
Create Date: 2020-02-18 11:52:47.407622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c8bd1b7c70a'
down_revision = '9b52c8db3c9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('customer_details', 'customer_email',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('customer_details', 'customer_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('customer_details', 'total_shopping_by_customer',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('customer_details', 'total_shopping_by_customer',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('customer_details', 'customer_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('customer_details', 'customer_email',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    # ### end Alembic commands ###
