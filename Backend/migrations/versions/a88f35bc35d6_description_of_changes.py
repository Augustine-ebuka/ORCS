"""Description of changes

Revision ID: a88f35bc35d6
Revises: 943ba57df06c
Create Date: 2023-12-22 23:52:48.611322

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a88f35bc35d6'
down_revision = '943ba57df06c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=mysql.VARCHAR(length=32),
               type_=sa.String(length=40),
               existing_nullable=True)
        batch_op.alter_column('matric_no',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.String(length=16),
               existing_nullable=False)
        batch_op.alter_column('middle_name',
               existing_type=mysql.VARCHAR(length=32),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.alter_column('middle_name',
               existing_type=mysql.VARCHAR(length=32),
               nullable=False)
        batch_op.alter_column('matric_no',
               existing_type=sa.String(length=16),
               type_=mysql.VARCHAR(length=10),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.String(length=40),
               type_=mysql.VARCHAR(length=32),
               existing_nullable=True)

    # ### end Alembic commands ###
