from pydantic import BaseModel

class Order(BaseModel):
    customer_name: str
    order_detail: str
    product_name: str
    quantity: int