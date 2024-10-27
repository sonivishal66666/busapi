# app/routes.py
from fastapi import APIRouter, HTTPException, status
from app.database import blog_collection
from app.models import BlogModel, BlogUpdateModel
from bson import ObjectId

router = APIRouter()

@router.post("/", response_description="Add new blog")
async def create_blog(blog: BlogModel):
    blog = blog.dict()
    result = await blog_collection.insert_one(blog)
    blog["_id"] = str(result.inserted_id)
    return blog

@router.get("/{id}", response_description="Get a single blog")
async def get_blog(id: str):
    if (blog := await blog_collection.find_one({"_id": ObjectId(id)})) is not None:
        blog["_id"] = str(blog["_id"])
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@router.put("/{id}", response_description="Update a blog")
async def update_blog(id: str, blog: BlogUpdateModel):
    if blog.dict(exclude_unset=True):
        result = await blog_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": blog.dict(exclude_unset=True)}
        )
        if result.modified_count == 1:
            updated_blog = await blog_collection.find_one({"_id": ObjectId(id)})
            updated_blog["_id"] = str(updated_blog["_id"])
            return updated_blog
    raise HTTPException(status_code=404, detail="Blog not found")

@router.delete("/{id}", response_description="Delete a blog")
async def delete_blog(id: str):
    result = await blog_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")
