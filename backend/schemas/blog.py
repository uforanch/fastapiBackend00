from typing import Optional
from pydantic import BaseModel, validator, field_validator
from datetime import date, datetime


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str]

    @validator('slug', pre=True)
    def generate_slug(cls, slug, values):
        title = values.get('title')
        slug = None
        if title:
            slug = title.replace(" ", "-").lower()
        return slug


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