"""Peewee migrations -- 001_auto.py.

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

    @migrator.create_model
    class Article(pw.Model):
        uid = pw.CharField(max_length=32, primary_key=True)
        create_user_id = pw.CharField(index=True, max_length=24)
        create_time = pw.DateTimeField(null=True)
        update_time = pw.DateTimeField(null=True)
        deleted = pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1)
        title = pw.CharField(index=True, max_length=32, null=True)
        content_id = pw.TextField()
        comment_count = pw.IntegerField()
        upvote = pw.IntegerField()
        funny = pw.IntegerField()
        love = pw.IntegerField()
        surprise = pw.IntegerField()
        sad = pw.IntegerField()

        class Meta:
            table_name = "louis_article"

    @migrator.create_model
    class BaseModel(pw.Model):
        uid = pw.CharField(max_length=32, primary_key=True)
        create_user_id = pw.CharField(index=True, max_length=24)
        create_time = pw.DateTimeField(null=True)
        update_time = pw.DateTimeField(null=True)
        deleted = pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1)

        class Meta:
            table_name = "basemodel"

    @migrator.create_model
    class Comment(pw.Model):
        uid = pw.CharField(max_length=32, primary_key=True)
        create_user_id = pw.CharField(index=True, max_length=24)
        create_time = pw.DateTimeField(null=True)
        update_time = pw.DateTimeField(null=True)
        deleted = pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1)
        user_id = pw.CharField(max_length=32)
        comment_id = pw.TextField()
        father_id = pw.CharField(max_length=32)
        good_count = pw.IntegerField()

        class Meta:
            table_name = "louis_comment"

    @migrator.create_model
    class Dairy(pw.Model):
        uid = pw.CharField(max_length=32, primary_key=True)
        create_user_id = pw.CharField(index=True, max_length=24)
        create_time = pw.DateTimeField(null=True)
        update_time = pw.DateTimeField(null=True)
        deleted = pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1)
        title = pw.CharField(max_length=32)
        content = pw.TextField(null=True)

        class Meta:
            table_name = "louis_dairy"

    @migrator.create_model
    class Label(pw.Model):
        uid = pw.CharField(max_length=32, primary_key=True)
        create_user_id = pw.CharField(index=True, max_length=24)
        create_time = pw.DateTimeField(null=True)
        update_time = pw.DateTimeField(null=True)
        deleted = pw.CharField(constraints=[SQL("DEFAULT '0'")], max_length=1)
        name = pw.CharField(max_length=32)
        article_id = pw.CharField(max_length=32)

        class Meta:
            table_name = "louis_label"



def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    migrator.remove_model('louis_label')

    migrator.remove_model('louis_dairy')

    migrator.remove_model('louis_comment')

    migrator.remove_model('basemodel')

    migrator.remove_model('louis_article')
