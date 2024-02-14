"""create votes

Revision ID: 02f3677d9f65
Revises: 51b77c7ceb14
Create Date: 2023-11-03 21:58:31.284536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02f3677d9f65'
down_revision: Union[str, None] = '51b77c7ceb14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'votes',
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True, nullable=False),
        sa.Column('post_id', sa.Integer(), sa.ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    )
    pass

def downgrade():
    op.drop_table('votes')