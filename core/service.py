from . import database as _database, models as _models, schemas as _schemas
import sqlalchemy.orm as _orm
import passlib.hash as _hash

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)



def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_username(username: str, db: _orm.Session):
    return  db.query(_models.User).filter(_models.User.username==username).first()



async def create_user(user: _schemas.UserCreate, db:_orm.Session):
    password = _hash.bcrypt.hash(user.password)
    user_obj = _models.User(username=user.username, password=password)
    db.add(user_obj)
    db.commit()
    db.refresh()
    return user_obj