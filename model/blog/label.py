from model.base_model import BaseModel
from peewee import *

class Label(BaseModel):
    name = CharField(32,verbose_name='标签')
    article_id = CharField(32,verbose_name='文章id')

    class Meta:
        table_name = "louis_label"