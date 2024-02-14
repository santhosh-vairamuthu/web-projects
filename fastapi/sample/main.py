from fastapi import FastAPI, Request, Depends,Form,HTTPException, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import engine, SessionLocal, get_db, Base
import model,schemas


app = FastAPI()
templates = Jinja2Templates(directory='templates')
Base.metadata.create_all(bind=engine)

@app.get("/")
def root(request: Request, db : Session = Depends(get_db)):
    order = db.query(model.Order).all()
    return templates.TemplateResponse("/index.html", {"request": request, "order" : order})


@app.post("/root_post")
def root_post(request: Request,db: Session = Depends(get_db),customerName: str = Form(...),orderDetails: str = Form(...),productName: str = Form(...),quantity: int = Form(...),):
    try:
        print(customerName)
        data = model.Order(
            customer_name=customerName,
            order_detail=orderDetails,
            product_name=productName,
            quantity=quantity,
        )
        db.add(data)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    return JSONResponse(content={"status": "Done"})

@app.delete("/root_delete")
def root_delete(request: Request,db: Session = Depends(get_db),id: int = Form(...)):
    try:
        del_post = db.query(model.Order).filter(model.Order.id == id)
        del_post_data = del_post.first()
        del_post.delete(synchronize_session=False)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    return JSONResponse(content={"status": "Done"})



@app.put("/put_data/{id}")
def put_data(id: int, request: Request, db: Session = Depends(get_db)):
    try:
        data = db.query(model.Order).filter(model.Order.id == id).first()
        if data is None:
            raise HTTPException(status_code=404, detail="Data not found")
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    
    return {"data": data}

@app.put("/put_post_edit")
def put_post_edit(request: Request,db: Session = Depends(get_db),id: int = Form(...),customerName: str = Form(...),orderDetails: str = Form(...),productName: str = Form(...),quantity: int = Form(...),):
    try:
        updated_post = db.query(model.Order).filter(model.Order.id == id)
        post_present = updated_post.first()
        if post_present is None:
            raise HTTPException(status_code=404, detail="Post not found")
        updated_post.update({
            model.Order.customer_name: customerName,
            model.Order.order_detail: orderDetails,
            model.Order.product_name: productName,
            model.Order.quantity: quantity,
        }, synchronize_session=False)
        db.commit()
    except Exception as e:
        print("Error updating post:", str(e))
        raise HTTPException(status_code=422, detail=str(e))

    return JSONResponse(content={"status": "Done"})


