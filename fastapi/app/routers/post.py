from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models,schemas,database,oauth2 
from .. database import  get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user), limit: int = 100, skip: int = 0, search: Optional[str] = ""):
    my_posts_with_votes = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.user_id == current_user.id).limit(limit).offset(skip).all()
    return my_posts_with_votes


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.PostOut)
def get_post(id : int, db : Session = Depends(get_db)):
    my_posts_with_votes = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not my_posts_with_votes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"NO post with id {id}.")
    return my_posts_with_votes


@router.post("/", status_code=status.HTTP_200_OK, response_model=schemas.Post)
def post_posts(post : schemas.CreatePost, db : Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    new_post = models.Post(user_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete("/{id}")
def delete_post(id:int, db : Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user)):
    del_post = db.query(models.Post).filter(models.Post.id == id)
    del_post_data = del_post.first()

    if del_post_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"NO post with id {id}.")

    if del_post_data.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Sry you don't own this post")

    del_post.delete(synchronize_session=False)
    
    db.commit()
    return {"data" : "post deleted successfully"}


@router.put("/{id}", response_model=schemas.Post)
def update_post(id : int, post: schemas.PostStruct, db : Session = Depends(get_db)):
    updated_post = db.query(models.Post).filter(models.Post.id == id)
    post_present = updated_post.first()
    if not post_present:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post with id {id}.")
    updated_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return updated_post.first()



