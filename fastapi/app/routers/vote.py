from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas,database, oauth2
from .. database import  get_db

router = APIRouter(
    prefix="/vote", 
    tags=["Vote"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def up_vote(vote : schemas.Vote, db : Session = Depends(database.get_db), current_user: str = Depends(oauth2.get_current_user)):
    find_post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if find_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {vote.post_id} not found")
    vote_query = db.query(models.Vote).filter(models.Vote.user_id==current_user.id,models.Vote.post_id==vote.post_id)
    find_vote = vote_query.first()
    if vote.dir == 1:
        if find_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.id} already voted")
        new_vote = models.Vote(user_id = current_user.id, post_id=vote.post_id)
        db.add(new_vote)
        db.commit()
        return {"msg" : "Voting Successfull"}
    else:
        if find_vote==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"msg" : "Down Voting Successfull"}