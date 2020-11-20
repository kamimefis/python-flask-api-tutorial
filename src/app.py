from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)


todos= [{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text= jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    adding_todo= todos.append(decoded_object)
    json_text= jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    request_body = request.data
    delete_todo= todos.pop(position)
    json_text= jsonify(todos)
    return json_text  



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)