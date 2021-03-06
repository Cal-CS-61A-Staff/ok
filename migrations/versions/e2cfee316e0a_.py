"""Add web submission changes

Revision ID: e2cfee316e0a
Revises: ed0359c3b84b
Create Date: 2016-08-08 16:41:43.369433

"""

# revision identifiers, used by Alembic.
revision = 'e2cfee316e0a'
down_revision = 'ed0359c3b84b'

from alembic import op
import sqlalchemy as sa
import server


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assignment', sa.Column('upload_info', sa.Text(), nullable=True))
    op.add_column('assignment', sa.Column('uploads_enabled', sa.Boolean(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assignment', 'uploads_enabled')
    op.drop_column('assignment', 'upload_info')
    ### end Alembic commands ###
