"""empty message

Revision ID: 449481e0ab21
Revises: ab0b9bf84830
Create Date: 2023-09-12 11:35:30.938244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '449481e0ab21'
down_revision = 'ab0b9bf84830'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
