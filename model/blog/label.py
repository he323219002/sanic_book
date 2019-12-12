from model.base_model import BaseModel
from peewee import *
from utils.uid import gen_id
from playhouse.signals import post_save

class Label(BaseModel):
    name = CharField(32,verbose_name='标签')
    article_id = CharField(32,verbose_name='文章id')

    class Meta:
        table_name = "louis_label"

@post_save(sender=Label)
def louis_label_handler(sender,instance=None,created=False,**kwargs):
    if instance.uid:
        uid = gen_id()
        instance.uid = f'{uid}'
