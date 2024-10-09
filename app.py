from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from configs import configs_env
from infra.repositories.todo_repository import TodoRepository

app = Flask(__name__) # __name__ == __main__

todo_repository = TodoRepository()

@app.route('/create', methods=['POST'])
def create_todo():
  data: any = request.form
  required_fields = ['title']
  
  for field in required_fields:
    if field not in data:
      return jsonify({"error": f"Invalid Param: {field}"}), 400

  title = data.get('title')
  
  todo_repository.create_todo(title)
  return jsonify({"message": "deu certo"}), 200

@app.route('/list')
def list_todos():
  todos = todo_repository.get_all_todos()
  todos = [t.to_dict() for t in todos]

  return jsonify({"todos": todos}), 200

if __name__ == '__main__':
  app.run(debug=True, host="localhost", port="4000")