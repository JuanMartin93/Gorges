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

