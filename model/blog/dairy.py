from model.base_model import BaseModel
from peewee import *
from utils.uid import gen_id
from playhouse.signals import pre_save,post_save

class Dairy(BaseModel):
    title = CharField(32, verbose_name='标题')
    content = TextField(32, verbose_name='内容')



    class Meta:
        table_name = "louis_dairy"

@pre_save(sender=Dairy)
def pre_save_handler(sender,instance,created=False,**kwargs):
    if not instance.uid:
        uid = gen_id()
        instance.uid = f'{uid}'
