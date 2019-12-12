from werkzeug.security import generate_password_hash,check_password_hash
from model import base_model
from peewee_migrate import Router
from model.blog.article import Article,Comment
from model.blog.dairy import Dairy
from model.system.user import User
import traceback


router = Router(base_model.db)

def migrate():
    router.create()
    router.run()


if __name__ == '__main__':
    try:
        base_model.db.create_tables([Article,Comment,Dairy,User])
    except Exception:
        # traceback.print_exc()
        pass
    test_obj = Dairy(
        title='xxx',
        content='232'
    )
    test_obj.save()
    # migrate()

