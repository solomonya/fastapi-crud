"""init

Revision ID: ea71c3b3094a
Revises: 
Create Date: 2022-11-18 15:06:00.735516

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'ea71c3b3094a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password_hash', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('speciality',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('code', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('department',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('foundation_date', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sgroup',
    sa.Column('code', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('specialily_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['specialily_id'], ['speciality.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('discipline',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('lection_hours', sa.Integer(), nullable=False),
    sa.Column('practice_hours', sa.Integer(), nullable=False),
    sa.Column('credits', sa.Integer(), nullable=False),
    sa.Column('semester', sa.Integer(), nullable=False),
    sa.Column('course', sa.Integer(), nullable=False),
    sa.Column('rgr_amount', sa.Integer(), nullable=False),
    sa.Column('srsp_hours', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('middle_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('perfomance', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('study_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['study_group_id'], ['sgroup.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher',
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('middle_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('academic_degree', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('hiring_date', sa.Date(), nullable=False),
    sa.Column('position', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password_hash', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher')
    op.drop_table('student')
    op.drop_table('discipline')
    op.drop_table('sgroup')
    op.drop_table('department')
    op.drop_table('speciality')
    op.drop_table('admin')
    # ### end Alembic commands ###
