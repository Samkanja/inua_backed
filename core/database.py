import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "sqlite:///./inua.db"

engine = _sql.create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal = _orm.sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = _declarative.declarative_base()