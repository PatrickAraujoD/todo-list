from flask import Flask, jsonify, request

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

@app.route('/update/<int:id_todo>', methods=['PUT'])
def update_todo(id_todo):
  data = request.get_json()
  required_fields = ['complete']
  
  for field in required_fields:
    if field not in data:
      return jsonify({"error": "Invalid Param: {field}"}), 400

  todo = todo_repository.get_todo_by_id(id_todo)
  
  if not todo:
    return jsonify({"error": "Tarefa não foi encontrada"}), 404
  
  complete = data.get('complete')
  
  is_save = todo_repository.update_todo_complete(id_todo, complete)
  
  if not is_save:
    return jsonify({"error": "Não foi possível finalizar a tarefa"}), 500

  return jsonify({"message": "atualizado com sucesso!"}), 200

@app.route('/delete/<int:id_todo>', methods=["DELETE"])
def delete_todo(id_todo):
  todo = todo_repository.get_todo_by_id(id_todo)
  
  if not todo:
    return jsonify({"error": "Tarefa não foi encontrada"}), 404

  deleted = todo_repository.delete_todo(todo)
  
  if not deleted:
    return jsonify({"error": "Não foi possivel deletar a tarefa"}), 500
  
  return jsonify({"message": "Tarefa deletada com sucesso"}), 200

if __name__ == '__main__':
  app.run(debug=True, host="localhost", port="4000")