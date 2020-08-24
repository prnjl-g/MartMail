"""empty message

Revision ID: 37502c1f9421
Revises: 7efcd665f1c8
Create Date: 2020-02-18 10:13:20.402044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37502c1f9421'
down_revision = '7efcd665f1c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_templates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_type', sa.String(length=30), nullable=True),
    sa.Column('is_template_approved', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_email_templates_email_type'), 'email_templates', ['email_type'], unique=False)
    op.create_index(op.f('ix_email_templates_is_template_approved'), 'email_templates', ['is_template_approved'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_email_templates_is_template_approved'), table_name='email_templates')
    op.drop_index(op.f('ix_email_templates_email_type'), table_name='email_templates')
    op.drop_table('email_templates')
    # ### end Alembic commands ###
