"""empty message

Revision ID: 01d0d8b09683
Revises: a4d328c070da
Create Date: 2020-02-18 11:44:28.840405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01d0d8b09683'
down_revision = 'a4d328c070da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('email_templates', 'email_content',
               existing_type=sa.VARCHAR(length=5000),
               nullable=False)
    op.alter_column('email_templates', 'email_type',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
    op.alter_column('email_templates', 'is_template_approved',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('email_templates', 'is_template_approved',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('email_templates', 'email_type',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
    op.alter_column('email_templates', 'email_content',
               existing_type=sa.VARCHAR(length=5000),
               nullable=True)
    # ### end Alembic commands ###
