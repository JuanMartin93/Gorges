from flask import jsonify, request, render_template
from datetime import datetime
from todo import app
import json
import requests
from pprint import pprint



@app.route('/favorites', methods=['GET'])
def get_controller():
  return jsonify("db.get_favorites()")


@app.route('/restaurants', methods=['GET'])
def get_controller2():
    url="https://api.yelp.com/v3/businesses/search?latitude=42.4440&longitude=-76.5019 "
    token = "HrbGqab1djPwIkoiMmilgN4kCdjkmEGHFGCgJet4UBAeW24cGNJocrmU-Zj3xez9-D0Ha1vXWfxLt6CxZywuKMYETU3KR5ZNwVSjeOnek9UWWaJALqip_aVnj8jsWnYx";
    r = requests.get(url, headers = {"Authorization":"Bearer " + token})

    r.content
    # data = []
    # for item in r.content["businesses"]:
    #     print(str(item))
    #     data.append({'name':item['name'], 'image':item['image_url'],'rating':item['rating'],'location':item['location']})
    # jsonData = json.dumps(data)

    return r.content['businesses']

@app.route('/events', methods=['GET'])
def get_controller3():
  return jsonify(db.get_favorites())

@app.route('/natural-attractions', methods=['GET'])
def get_controlle4():
  return jsonify(db.get_favorites())
