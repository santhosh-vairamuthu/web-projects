from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body 
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

# general SQL Query Methods

class PostStruct(BaseModel):
    title: str
    content: str
    published: bool = True


while True:
    try:
        conn = psycopg2.connect(host='localhost', port="5432",database="fastapi",user="postgres",password="testpass",cursor_factory=RealDictCursor)
        cursor  = conn.cursor()
        print("DB connection established")
        break
    except Exception as e:
        print("Failure in DB connection:" + str(e))
        time.sleep(2)

def commit_changes():
    conn.commit()



@app.get("/")
def root():
    return {
        "message": "Hello World",
        "name":"Santhosh"
    }

@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts""")
    my_posts  = cursor.fetchall()
    return {"data" : my_posts}


@app.get("/posts/{id}")
def get_post(id : int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s""", (str(id)))
    my_post = cursor.fetchone()
    if not my_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"NO post with id {id}.")
    return {"data": my_post}




@app.post("/posts",status_code=status.HTTP_201_CREATED)
def post_posts(post: PostStruct):
    # Vulnerable Approach.Prone to sql injection attacks
    # cursor.execute(f""" INSERT INTO posts (title, content) VALUES ('{post.title}', '{post.content}')""")

    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING *", (post.title, post.content))
    commit_changes()
    my_post = cursor.fetchone()
    return  {"data" : my_post}



@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),), )
    deleted_post = cursor.fetchone()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post with id {id}.")
    commit_changes()
    return {"data": "Post deleted successfully"}


@app.put("/posts/{id}")
def update_post(id : int, post: PostStruct):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post with id {id}.")
    commit_changes()
    return {"data": "Post Updated successfully"}
