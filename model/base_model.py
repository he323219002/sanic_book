from peewee import MySQLDatabase, Model, CharField, DateTimeField
from playhouse.pool import PooledMySQLDatabase
from utils import timezone
from playhouse.signals import Model as Signal_Model

db = PooledMySQLDatabase("louis", host="127.0.0.1", port=3306,
                         user='root', password='he123456', charset='utf8mb4',
                         max_connections=4)


class BaseModel(Signal_Model):
    uid = CharField(verbose_name='ID', max_length=32, index=True, unique=True, primary_key=True)
    create_user_id = CharField(verbose_name='创建用户id', max_length=24, index=True, default='')
    create_time = DateTimeField(verbose_name='创建时间', default=timezone.now())
    update_user_id = CharField(verbose_name='更新用户id', max_length=24, index=True, null=True, default='')
    update_time = DateTimeField(verbose_name='更新时间', default=timezone.now())
    deleted = CharField(verbose_name='已删除', max_length=1, default='0')

    class Meta:
        database = db

    def save(self, *args, **kwargs):
        super().save(force_insert=True)

    def save_with_log(self, user_id):
        if not self.create_user_id:
            self.create_user_id = user_id
        self.update_user_id = user_id
        if not self.create_time:
            self.create_time = timezone.now()
        self.save()
