from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base, engine


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    customer_name = Column(String(255), nullable=False)
    order_detail = Column(String(255), nullable=False)
    product_name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
