from datetime import datetime
from bson import ObjectId

from app.database import blogs_collection

class BlogService:


    @staticmethod 
    async def create_blog(blog, current_user):

        blog_data = blog.model_dump()

        blog_data["author_id"] = str(current_user["id"])

        blog_data["created_at"] = datetime.utcnow()

        result = await blogs_collection.insert_one(blog_data)

        blog_data["_id"] = str(result.inserted_id)

        return blog_data






















