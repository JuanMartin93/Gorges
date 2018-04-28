import os
import json
import sqlite3
from todo.models import Task

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
    self.conn = sqlite3.connect("todo.db", check_same_thread=False)
    self.create_task_table()

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

  def create_task_table(self):
    try:
      self.conn.execute (""" 
      CREATE TABLE tasks 
      (
        DUE_DATE INT NOT NULL,
        DESCRIPTION TEXT NOT NULL,
        TAGS TEXT NOT NULL,
        CREATED_AT INT NOT NULL,
        ID TEXT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL
      )
      """)
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
