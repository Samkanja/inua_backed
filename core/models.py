import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash


from . import database as _database


class User(_database.Base):
    __tablename__ = "users"

    id = _sql.Column(_sql.Integer, primary_key=True,index=True)
    username = _sql.Column(_sql.String, unique=True,index=True)
    password = _sql.Column(_sql.String)
    programs = _orm.relationship("Program", back_populates="owner")

    def verity_password(self, password: str):
        return _hash.bcrypt.verify(password, self.password)


class Program(_database.Base):
    __tablename__ = 'programs'

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, unique=True)
    content = _sql.Column(_sql.String)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    image_file = _sql.Column(_sql.String)
    owner = _orm.relationship("User", back_populates="programs")