from pydantic import BaseModel, EmailStr, Field

#pydantic is basically DTOS but advanced - completely seperating entity and dto

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)

#note it's nice we can have multiple user-related DTO's same file, java we'd need to make a big folder
class ShowUser(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    class config():#tell pydantic to convert even non dict object to json
        orm_mode=True

