from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    if "label" not in request_body or "done" not in request_body:
        return jsonify({"msg": "Invalid input"}), 400
    todos.append(request_body)
    return jsonify(todos)
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos), 200
    else:
        return jsonify({"msg": "Position out of range"}), 404  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)