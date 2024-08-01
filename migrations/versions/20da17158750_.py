"""empty message

Revision ID: 20da17158750
Revises: ed354307d20b
Create Date: 2024-08-01 18:32:03.553499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20da17158750'
down_revision = 'ed354307d20b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('influencers', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('sponcers', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sponcers', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('influencers', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###