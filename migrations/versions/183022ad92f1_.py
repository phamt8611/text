"""empty message

Revision ID: 183022ad92f1
Revises: 
Create Date: 2020-10-23 22:56:37.503104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183022ad92f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('novel',
    sa.Column('ids', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('ids'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('post',
    sa.Column('ids', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('authur', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('ids'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tag',
    sa.Column('ids', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('ids'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('novels_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('novel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['novel_id'], ['novel.ids'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('posts_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tags_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.ids'], ),
    sa.ForeignKeyConstraint(['tags_id'], ['tag.ids'], )
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_users')
    op.drop_table('posts_tags')
    op.drop_table('novels_users')
    op.drop_table('user')
    op.drop_table('tag')
    op.drop_table('role')
    op.drop_table('post')
    op.drop_table('novel')
    # ### end Alembic commands ###