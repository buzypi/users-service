from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps
import os

app = Flask(__name__)
client = MongoClient(host=os.environ['DB_HOST'])
db = client.usersdb

# This is only for the purpose of demo
if db.user.count_documents({}) == 0:
  db.user.insert({'name': 'John'})
  db.user.insert({'name': 'George'})


@app.route('/')
def hello():
  return 'Hello world!'


@app.route('/users')
def users():
  users_list = []
  for user in db.user.find():
    users_list.append(user)
  return dumps(users_list)
