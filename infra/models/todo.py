from typing import Type
from sqlalchemy import Boolean, Column, Integer, String
from infra.configs.base import Base


class Todo(Base):
  __tablename__ = 'todo'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(200), nullable=False)
  complete = Column(Boolean, nullable=False, default=False)
  
  def __init__(self, title: str) -> None:
    self.title = title
  
  def __repr__(self):
    return '{ "id": self.id, "title": self.title, "complete": self.complete }'
  