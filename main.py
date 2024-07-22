import fastapi as _fastapi
import uvicorn as _uvicorn
import core.service as _service
import core.schemas as _schemas
import sqlalchemy.orm as _orm


app = _fastapi.FastAPI()

@app.post("/api/users")
async def create_user(user: _schemas.User, db : _orm.Session=_fastapi.Depends(_service.get_db)):
    db_user = _service.get_user_by_username(user.username, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Username already exits")
    return await _service.create_user(user, db)
    


