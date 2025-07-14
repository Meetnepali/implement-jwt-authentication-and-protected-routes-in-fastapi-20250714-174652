from pydantic import BaseModel, EmailStr, Field
from typing import List

class OrderCreate(BaseModel):
    product_name: str = Field(..., example="Book")
    quantity: int = Field(..., gt=0)
    customer_email: EmailStr

class OrderOut(BaseModel):
    id: int
    product_name: str
    quantity: int
    customer_email: EmailStr
    status: str
    class Config:
        orm_mode = True

class OrderStatusOut(BaseModel):
    id: int
    status: str
    class Config:
        orm_mode = True
