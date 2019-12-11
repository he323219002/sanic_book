from peewee import Model, CharField, BooleanField, DateTimeField, IntegerField
from model import base_model as BaseModel
from utils import timezone
from werkzeug.security import generate_password_hash,check_password_hash
from settings import config


class User(Model):
    uid = CharField(verbose_name='用户id', max_length=32, index=True, unique=True, primary_key=True)
    username = CharField(verbose_name='用户名', max_length=24)
    password = CharField(128, verbose_name='密码')
    last_login = DateTimeField(verbose_name='last_login', default=timezone.now())
    phone = CharField(verbose_name='手机号', null=True, max_length=13)
    nickname = CharField(verbose_name='昵称', max_length=24, null=True)
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    register_time = DateTimeField(null=True, default=timezone.now())
    version = IntegerField(verbose_name='密码版本', default=1)
    email = CharField(20,verbose_name='邮箱',null=True)
    # 0女1男
    gender = CharField(1, verbose_name='性别', default='1')
    avatar = CharField(256, verbose_name='头像', default='')
    # 0普通用户 1管理员
    role = CharField(1, verbose_name='角色', default='0')
    deleted = CharField(1, verbose_name='是否删除', default='0')

    def __str__(self):
        return self.get_username()

    def set_password(self,raw_password):
        self.password = generate_password_hash(raw_password)
        return self.password

    def check_password(self,raw_password):
        return check_password_hash(self.password,raw_password)

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

    class Meta:
        table_name = 'system_user'
