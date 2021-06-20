from alembic import op
import sqlalchemy as sa


revision = '654da5778cac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=4096), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False, unique=False),
    sa.Column('title', sa.String(length=4096), nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('provider', sa.String(length=4096), nullable=False),
    sa.ForeignKeyConstraint(['category'], ['category.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('course', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course'], ['course.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('review')
    op.drop_table('course')
    op.drop_table('category')
