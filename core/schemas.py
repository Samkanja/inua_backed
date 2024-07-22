import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    username: str


class UserCreate(_UserBase):
    password : str

    class Config:
        from_attributes = True
    
class User(_UserBase):
    id: int

    class Config:
        from_attributes = True




class _ProgramBase(_pydantic.BaseModel):
    title: str
    content: str
    image_file: str


class Program(_ProgramBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True