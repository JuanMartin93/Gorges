from flask import jsonify, request, render_template
from todo import app
from todo import Db as db
from todo.models import Task
from datetime import datetime
import json

@app.route('/', methods=['GET'])
def index():
  return jsonify({"HELLO": "WORLD"})

@app.route('/tasks/all', methods=['DELETE'])
def delete_all_controller(): 
  db.delete_all_task()
  return jsonify({"success": "true"})

@app.route('/tasks', methods=['POST', 'GET', 'DELETE'])
def post_controller():

  if request.method == 'POST':
    name = request.args['name']
    description = request.args['description']
    tags = request.args['tags']
    due_date = request.args['due_date']

    task = Task(due_date, description, tags, name)
    db.insert_task_table(task)

    return jsonify(task.to_dict())

  if request.method == 'GET':
    if request.args.get('id'): 
      id  = request.args.get('id')
      return jsonify(db.get_task(id))
    print "getting here"
    return jsonify(db.get_all_tasks())

  if request.method == 'DELETE':
    if request.args.get('id'): 
      id  = request.args.get('id')
      db.delete_task(id)
    return jsonify({"success": "true"}) 