from typing import Optional
from pydantic import BaseModel, validator, field_validator,root_validator
from datetime import date, datetime

#equivalent of dtos
class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str]

    @root_validator(pre=True)
    def generate_slug(cls, values):
        print("***",values, "***")
        title = values.get('title')

        if title:
            values['slug'] = title.replace(" ", "-").lower()
        return values


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: date
    class Config():
        orm_mode = True
    @field_validator('created_at', mode='before')
    def format_date(cls, v):
        if isinstance(v, datetime):
            return v.date()
        return v

class UpdateBlog(CreateBlog):
    pass