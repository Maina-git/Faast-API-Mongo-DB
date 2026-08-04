from pydantic import BaseModel

class CreateBlog(BaseModel):
    title: str
    text: str





