"""Peewee migrations -- 003_auto.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['model_name']            # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.python(func, *args, **kwargs)        # Run python code
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.drop_index(model, *col_names)
    > migrator.add_not_null(model, *field_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)

"""

import datetime as dt
import peewee as pw
from decimal import ROUND_HALF_EVEN

try:
    import playhouse.postgres_ext as pw_pext
except ImportError:
    pass

SQL = pw.SQL


def migrate(migrator, database, fake=False, **kwargs):
    """Write your migrations here."""

    migrator.change_fields('louis_article', create_user_id=pw.CharField(constraints=[SQL("DEFAULT ''")], index=True, max_length=24),
        deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))

    migrator.change_fields('basemodel', create_user_id=pw.CharField(constraints=[SQL("DEFAULT ''")], index=True, max_length=24),
        deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))

    migrator.change_fields('louis_comment', create_user_id=pw.CharField(constraints=[SQL("DEFAULT ''")], index=True, max_length=24),
        deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))

    migrator.change_fields('louis_dairy', create_user_id=pw.CharField(constraints=[SQL("DEFAULT ''")], index=True, max_length=24),
        deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))

    migrator.drop_not_null('louis_dairy', 'content')

    migrator.change_fields('louis_label', create_user_id=pw.CharField(constraints=[SQL("DEFAULT ''")], index=True, max_length=24),
        deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))


def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    migrator.drop_not_null('louis_dairy', 'content')
