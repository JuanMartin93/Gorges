import os
import json
import sqlite3
from todo import app
from flaskext.mysql import MySQL

# From: https://goo.gl/YzypOI
def singleton(cls):
  instances = {}
  def getinstance():
    if cls not in instances:
      instances[cls] = cls()
    return instances[cls]
  return getinstance

class DB(object):
  """
  DB driver for the Todo app - deals with writing entities
  to the DB and reading entities from the DB
  """

  def __init__(self):
    # self.conn = sqlite3.connect("todo.db", check_same_thread=False)
    mysql = MySQL()

    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'GORGES'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    self.cursor = mysql.connect().cursor()

    # result = self.create_favorites_table()

  def row_cursor(self, cursor):

    response = []
    for row in cursor:
      print row
      response.append(
        {
          'due_date' : row[0],
          'description' : row[1],
          'tags' : row[2],
          'created_at' : row[3],
          'id' : row[4],
          'name': row[5]
        }
      )
    return response

  def get_favorites(self):
    data = self.cursor.execute("select * from user_favorites;")
    # print(str(self.cursor.fetchall()))

    return self.cursor.fetchall()

  def create_favorites_table(self):
    try:
      query = """
          CREATE TABLE user_favorites
          (
            place_id BIGINT NOT NULL AUTO_INCREMENT,
            place_name VARCHAR(45) NOT NULL,
            place_location VARCHAR(45) NULL,
            PRIMARY KEY (`place_id`)
          )
        """

      self.cursor.execute(query)
      query = "INSERT INTO user_favorites (place_name, place_location) VALUES (\"Ithaca Falls\", \"3 miles south from west\")"
      print("query" + query)
      self.cursor.execute(query)

    except Exception as e: print e



# Only <=1 instance of the DB driver
# exists within the app at all times
DB = singleton(DB)
