from model.base_model import BaseModel
from peewee import *

class Article(BaseModel):
    title = CharField(32,verbose_name='标题',null=True,index=True)
    content_id = TextField(verbose_name='内容')
    comment_count = IntegerField(verbose_name='评论数')
    upvote = IntegerField(verbose_name='点赞')
    funny = IntegerField(verbose_name='点赞开心')
    love = IntegerField(verbose_name='点赞喜欢')
    surprise = IntegerField(verbose_name='点赞惊讶')
    sad = IntegerField(verbose_name='点赞悲伤')

    class Meta:
        table_name = "louis_article"


class Comment(BaseModel):
    user_id = CharField(32,verbose_name='用户id')
    comment_id = TextField(verbose_name='内容')
    father_id = CharField(32,verbose_name='父评论id')
    good_count = IntegerField(verbose_name='点赞数')

    class Meta:
        table_name = "louis_comment"