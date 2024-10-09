from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from configs import configs_env
from infra.repositories.todo_repository import TodoRepository
from routes import initialize_routes

app = Flask(__name__) # __name__ == __main__
initialize_routes(app)

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

if __name__ == '__main__':
  app.run(debug=True, host="localhost", port="4000")