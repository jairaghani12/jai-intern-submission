from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list of todos
todos = [
    {"id": 1, "task": "Learn Docker"},
    {"id": 2, "task": "Deploy to AWS EC2"}
]


@app.route('/')
def index():
    return "Todo API"


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "Task is required"}), 400
    new_todo = {
        "id": len(todos) + 1,
        "task": data['task']
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
