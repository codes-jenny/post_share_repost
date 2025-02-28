""" id

Revision ID: 45cf77e90c0f
Revises: 13298eb330c1
Create Date: 2024-11-23 13:44:55.639238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45cf77e90c0f'
down_revision = '13298eb330c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shared_posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sent_to_user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'users', ['sent_to_user_id'], ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shared_posts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('sent_to_user_id')

    # ### end Alembic commands ###
