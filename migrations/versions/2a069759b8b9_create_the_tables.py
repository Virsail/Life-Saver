"""create the tables

Revision ID: 2a069759b8b9
Revises: 
Create Date: 2020-09-26 10:02:06.251427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a069759b8b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'comment',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('comments', 'pitch_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    op.create_foreign_key(None, 'downvotes', 'pitches', ['pitch_id'], ['id'])
    op.create_foreign_key(None, 'downvotes', 'users', ['user_id'], ['id'])
    op.alter_column('pitches', 'category',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('pitches', 'post',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('pitches', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_index(op.f('ix_pitches_category'), 'pitches', ['category'], unique=False)
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.drop_column('pitches', 'downvote')
    op.drop_column('pitches', 'upvote')
    op.drop_column('pitches', 'comment')
    op.create_foreign_key(None, 'upvotes', 'pitches', ['pitch_id'], ['id'])
    op.create_foreign_key(None, 'upvotes', 'users', ['user_id'], ['id'])
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'secure_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'users', ['email'])
    op.create_unique_constraint(None, 'users', ['username'])
    op.drop_column('users', 'downvote')
    op.drop_column('users', 'upvote')
    op.drop_column('users', 'comment')
    op.drop_column('users', 'pitches')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pitches', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('upvote', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('downvote', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'secure_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.add_column('pitches', sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('upvote', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('downvote', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_index(op.f('ix_pitches_category'), table_name='pitches')
    op.alter_column('pitches', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('pitches', 'post',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('pitches', 'category',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comments', 'pitch_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comments', 'comment',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###