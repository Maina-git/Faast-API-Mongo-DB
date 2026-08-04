from fastapi import APIRouter, Depends
from app.models.blog import CreateBlog
from app.services.blog_service import BlogService
from app.utils.auth import get_current_user

router = APIRouter(
    prefix = "/blogs",
    tags = ["Blogs"]
 )



@router.post("/")
async def create_blog(
    blog: CreateBlog,
    current_user = Depends(get_current_user)):

  return await BlogService.create_blog(
    blog,
    current_user
  )




