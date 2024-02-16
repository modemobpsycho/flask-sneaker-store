"""new field in product

Revision ID: 262903cb4955
Revises: 803081241cb5
Create Date: 2024-02-16 00:22:10.395444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '262903cb4955'
down_revision = '803081241cb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('requires_size', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('requires_size')

    # ### end Alembic commands ###
