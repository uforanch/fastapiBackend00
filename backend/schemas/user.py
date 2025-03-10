from pydantic import BaseModel, EmailStr, Field

#pydantic is basically DTOS but advanced - completely seperating entity and dto

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)

