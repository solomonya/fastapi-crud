"""added study_load model

Revision ID: 01935b91e54d
Revises: 55b90e727b00
Create Date: 2022-11-26 10:22:20.276341

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '01935b91e54d'
down_revision = '55b90e727b00'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('load',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('discipline_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['discipline.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groupstudyloadlink',
    sa.Column('study_laod_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['sgroup.id'], ),
    sa.ForeignKeyConstraint(['study_laod_id'], ['load.id'], ),
    sa.PrimaryKeyConstraint('study_laod_id', 'group_id')
    )
    op.create_table('teacherstudyloadlink',
    sa.Column('study_load_id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['study_load_id'], ['load.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('study_load_id', 'teacher_id')
    )
    op.add_column('sgroup', sa.Column('speciality_id', sa.Integer(), nullable=True))
    op.drop_constraint('sgroup_ibfk_1', 'sgroup', type_='foreignkey')
    op.create_foreign_key(None, 'sgroup', 'speciality', ['speciality_id'], ['id'])
    op.drop_column('sgroup', 'specialily_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sgroup', sa.Column('specialily_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'sgroup', type_='foreignkey')
    op.create_foreign_key('sgroup_ibfk_1', 'sgroup', 'speciality', ['specialily_id'], ['id'])
    op.drop_column('sgroup', 'speciality_id')
    op.drop_table('teacherstudyloadlink')
    op.drop_table('groupstudyloadlink')
    op.drop_table('load')
    # ### end Alembic commands ###