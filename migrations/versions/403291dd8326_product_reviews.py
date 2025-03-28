"""product reviews

Revision ID: 403291dd8326
Revises: 713565e8fc50
Create Date: 2025-03-14 20:53:39.285453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '403291dd8326'
down_revision: Union[str, None] = '713565e8fc50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products_reviews',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Uuid(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_products_reviews_customer_id_customers')),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_products_reviews_product_id_products')),
    sa.PrimaryKeyConstraint('product_id', 'customer_id', name=op.f('pk_products_reviews'))
    )
    with op.batch_alter_table('products_reviews', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_products_reviews_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products_reviews', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_products_reviews_timestamp'))

    op.drop_table('products_reviews')
    # ### end Alembic commands ###
