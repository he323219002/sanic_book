from werkzeug.security import generate_password_hash,check_password_hash
from model import base_model
from peewee_migrate import Router
from model.blog.article import Article,Comment
from model import blog
from model.system import user
import sys
from os.path import abspath,join,dirname
from model.system.user import User
from utils.uid import gen_id

import traceback


def migrate():
    router.create()
    router.run()

# print(user.__path__)
# print(dairy.Dairy)
if __name__ == '__main__':

    # print(__file__.__path__)
    # try:
    #     base_model.db.create_tables([Article,Comment,Dairy,User])
    # except Exception:
    #     traceback.print_exc()
    #     pass

    # base_model.db.connect()
    router = Router(base_model.db)
    router.create(auto=blog)
    router.run()
    # base_model.db.close()

    # print(test_obj.content)
    # migrate()

