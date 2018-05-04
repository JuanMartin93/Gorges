from flask import jsonify, request, render_template
from todo import app
from todo import Db as db
from todo.models import Task
from datetime import datetime
import json


@app.route('/favorites', methods=['GET'])
def get_controller():
  return jsonify("db.get_favorites()")


@app.route('/restaurants', methods=['GET'])
def get_controller2():
  return jsonify("pinga")

@app.route('/events', methods=['GET'])
def get_controller3():
  return jsonify(db.get_favorites())

@app.route('/natural-attractions', methods=['GET'])
def get_controlle4():
  return jsonify(db.get_favorites())
<<<<<<< HEAD


@app.route('/tasks/all', methods=['DELETE'])
def delete_all_controller(): 
  db.delete_all_task()
  return jsonify({"success": "true"})



# @app.route('/tasks', methods=['POST', 'GET', 'DELETE'])
# def post_controller():

#   if request.method == 'POST':
#     name = request.args['name']
#     description = request.args['description']
#     tags = request.args['tags']
#     due_date = request.args['due_date']

#     task = Task(due_date, description, tags, name)
#     db.insert_task_table(task)

#     return jsonify(task.to_dict())

#   if request.method == 'GET':
#     if request.args.get('id'): 
#       id  = request.args.get('id')
#       return jsonify(db.get_task(id))
#     print "getting here"
#     return jsonify(db.get_all_tasks())

#   if request.method == 'DELETE':
#     if request.args.get('id'): 
#       id  = request.args.get('id')
#       db.delete_task(id)
#     return jsonify({"success": "true"}) 
=======
    
>>>>>>> 5a3c7c29c3f5bb78202a2542dbfd51cc65c963f4
