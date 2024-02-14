from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, default=True)
    createdAt = Column(TIMESTAMP(timezone = True), nullable=False, server_default = text('now()'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    owner = relationship("User")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, nullable=False, primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    createdAt = Column(TIMESTAMP(timezone = True), nullable=False, server_default = text('now()'))
    phone_number = Column(String(255))

class Vote(Base):
    __tablename__ = 'votes';

    user_id = Column(Integer, ForeignKey('users.id', ondelete="Cascade"), primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete="Cascade"), primary_key=True, nullable=False)