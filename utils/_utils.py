from werkzeug.security import generate_password_hash,check_password_hash
from model import base_model
from peewee_migrate import Router


router = Router(base_model.db)

def migrate():
    router.create()
    router.run()


if __name__ == '__main__':
    migrate()

