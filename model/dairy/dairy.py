from model.base_model import BaseModel
from peewee import *


class Dairy(BaseModel):
    title = CharField(32, verbose_name='标题')
    content = TextField(32, verbose_name='内容')


    class Meta:
        table_name = "louis_label"