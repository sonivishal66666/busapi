# app/models.py
from pydantic import BaseModel, Field
from typing import Optional

class BlogModel(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "title": "My First Blog Post",
                "content": "This is the content of the blog post.",
                "author": "John Doe"
            }
        }

class BlogUpdateModel(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    content: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1, max_length=50)
