from typing import Union

from sqlalchemy import update
from infra.configs.handler_db import HandlerDb
from infra.models.todo import Todo

class TodoRepository:
  def get_all_todos(self):
    with HandlerDb() as connection:
      todos = connection.session.query(Todo).all()
      print(todos)
      return todos
    
  def create_todo(self, title: str) -> Todo:
    with HandlerDb() as connection:
      try:
        todo: Todo = Todo(title=title)
        print(todo)
        connection.session.add(todo)
        connection.session.commit()
        return todo
      except:
        connection.session.rollback()
        raise
      finally:
        connection.session.close()
        
  def get_todo_by_id(self, id_todo: int) -> Union[Todo, None]:
    with HandlerDb() as connection:
      todo = connection.session.query(Todo).filter_by(id=id_todo).first()
      return todo
  
  def update_todo_complete(self, id_todo: int,  complete: bool) -> bool:
    with HandlerDb() as connection:
      try:
        stmt = (
          update(Todo)
          .where(Todo.id == id_todo)
          .values(complete=complete)
        )
        connection.session.execute(stmt)
        connection.session.commit()
        return True
      except Exception as e:
        print(e)
        connection.session.rollback()
        return False
      finally:
        connection.session.close()
        
  def delete_todo(self, todo: Todo) -> bool:
    with HandlerDb() as connection:
      try:
        connection.session.delete(todo)
        connection.session.commit()
        return True
      except:
        connection.session.rollback()
        return False
      finally:
        connection.session.close()