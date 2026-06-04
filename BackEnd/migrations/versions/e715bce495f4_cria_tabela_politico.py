"""cria tabela politico

Revision ID: e715bce495f4
Revises: 280ce7666635
Create Date: 2026-06-04 18:00:48.534826

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


revision: str = 'e715bce495f4'
down_revision: Union[str, Sequence[str], None] = '280ce7666635'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.create_table(
        'politicos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('crawler_id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(255), nullable=False),
        sa.Column('partido', sa.String(255), nullable=True),
        sa.Column('email', sa.String(255), nullable=True),
        sa.Column('telefone', sa.String(20), nullable=True),
        sa.Column('endereco', sa.String(255), nullable=True),
        sa.Column('data_nascimento', sa.DateTime(timezone=True), nullable=True),
        sa.Column('foto_url', sa.String(255), nullable=True),
        sa.Column('foto_path_sistema', sa.String(255), nullable=True),
        sa.Column('situacao', sa.String(50), nullable=True),
        sa.Column('ativo', sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['crawler_id'], ['crawlers.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('politicos')
