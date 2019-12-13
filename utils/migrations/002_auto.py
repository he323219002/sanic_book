"""Peewee migrations -- 002_auto.py.

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

    migrator.add_fields(
        'louis_article',

        update_user_id=pw.CharField(max_length=24, null=True))

    migrator.change_fields('louis_article', deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))

    migrator.add_index('louis_article', 'uid', unique=True)

    migrator.add_fields(
        'basemodel',

        update_user_id=pw.CharField(max_length=24, null=True))

    migrator.change_fields('basemodel', deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))

    migrator.add_index('basemodel', 'uid', unique=True)

    migrator.add_fields(
        'louis_comment',

        update_user_id=pw.CharField(max_length=24, null=True))

    migrator.change_fields('louis_comment', deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))

    migrator.add_index('louis_comment', 'uid', unique=True)

    migrator.add_fields(
        'louis_dairy',

        update_user_id=pw.CharField(max_length=24, null=True))

    migrator.change_fields('louis_dairy', deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))

    migrator.drop_not_null('louis_dairy', 'content')

    migrator.add_index('louis_dairy', 'uid', unique=True)

    migrator.add_fields(
        'louis_label',

        update_user_id=pw.CharField(max_length=24, null=True))

    migrator.change_fields('louis_label', deleted=pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1))

    migrator.add_index('louis_label', 'uid', unique=True)


def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    migrator.remove_fields('louis_label', 'update_user_id')

    migrator.drop_index('louis_label', 'uid')

    migrator.remove_fields('louis_dairy', 'update_user_id')

    migrator.drop_not_null('louis_dairy', 'content')

    migrator.drop_index('louis_dairy', 'uid')

    migrator.remove_fields('louis_comment', 'update_user_id')

    migrator.drop_index('louis_comment', 'uid')

    migrator.remove_fields('basemodel', 'update_user_id')

    migrator.drop_index('basemodel', 'uid')

    migrator.remove_fields('louis_article', 'update_user_id')

    migrator.drop_index('louis_article', 'uid')
