from fastapi import FastAPI
from app.routers import orders
from app.errors import add_exception_handlers
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
add_exception_handlers(app)

app.include_router(orders.router, prefix="/orders", tags=["orders"])
