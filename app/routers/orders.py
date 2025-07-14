from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas, background

router = APIRouter()

@router.post("/", response_model=schemas.OrderOut, status_code=201)
async def create_order(order_in: schemas.OrderCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_order = models.Order(**order_in.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    background_tasks.add_task(background.send_order_email, db_order.id, db_order.customer_email)
    return db_order

@router.get("/", response_model=list[schemas.OrderOut])
async def list_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router.get("/{order_id}/status", response_model=schemas.OrderStatusOut)
async def order_status(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
