import os
import json
import sqlite3
from todo.models import Task
from flaskext.mysql import MySQL
from todo import app

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
    app.config['MYSQL_DATABASE_USER'] = 'juan'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
    app.config['MYSQL_DATABASE_DB'] = 'GORGES'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    self.cursor = mysql.connect().cursor()

    result = self.create_favorites_table()

    print("result " + str(result))
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

  def delete_task_table(self):
    self.conn.execute("""
      DROP TABLE tasks;
      """)
    self.conn.commit()

  def delete_all_task(self): 
    self.conn.execute("""
    DELETE FROM tasks;
    """)
    self.conn.commit()

  def delete_task(self, id):
    self.conn.execute(""" 
      DELETE FROM tasks 
      WHERE ID = (?);
    """, [id])
    self.conn.commit()

  def insert_task_table(self, task): 
    self.conn.execute("""
      INSERT INTO tasks (DUE_DATE, DESCRIPTION, TAGS, CREATED_AT, ID, NAME)
      VALUES (?,?,?,?,?,?);""", (task.due_date, task.description, task.tags, task.created_at, task.id, task.name))
    self.conn.commit()

  def get_all_tasks(self): 
    cursor = self.conn.execute("select * from tasks;")
    return self.row_cursor(cursor)


  def get_task(self, id): 
    cursor = self.conn.execute("""
    Select * FROM tasks 
    WHERE ID = (?)
    """, [id])
    return self.row_cursor(cursor)

  def example_create_table(self):
    """
    Demonstrates how to make a table. Silently error-handles
    (try-except) because the table might already exist.
    """
    try:
      self.conn.execute("""
        CREATE TABLE example
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        ADDRESS CHAR(50) NOT NULL);
      """)
    except Exception as e: print e

  def example_query(self):
    """
    Demonstrates how to execute a query.
    """
    cursor = self.conn.execute("""
      SELECT * FROM example;
    """)

    for row in cursor:
      print "ID = ", row[0]
      print "NAME = ", row[1]
      print "ADDRESS = ", row[2], "\n"

  def example_insert(self):
    """
    Demonstrates how to perform an insert operation.
    """
    self.conn.execute("""
      INSERT INTO example (ID,NAME,ADDRESS)
      VALUES (1, "Joe", "Ithaca, NY");
    """)
    self.conn.commit()


# Only <=1 instance of the DB driver
# exists within the app at all times
DB = singleton(DB)
