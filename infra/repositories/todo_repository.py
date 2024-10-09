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