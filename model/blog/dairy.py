from model.base_model import BaseModel
from peewee import *
from utils.uid import gen_id
from playhouse.signals import post_save

class Dairy(BaseModel):
    title = CharField(32, verbose_name='标题')
    content = TextField(32, verbose_name='内容')


    class Meta:
        table_name = "louis_dairy"

@post_save(sender=Dairy)
def louis_label_dairy(sender,instance=None,created=False,**kwargs):
    if instance.uid:
        uid = gen_id()
        instance.uid = f'{uid}'


class DataTest(BaseModel):
    name = CharField(32)
    age = IntegerField()

    class Meta:
        table_name = 'louis_test'