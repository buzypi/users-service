from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps
import os

app = Flask(__name__)
client = MongoClient(host=os.environ['DB_HOST'])
db = client.usersdb

# This is only for the purpose of demo
if db.user.count_documents({}) == 0:
  db.user.insert({'userid': 1, 'name': 'John'})
  db.user.insert({'userid': 2, 'name': 'George'})


@app.route('/ping')
def ping():
  return 'pong'


@app.route('/users')
def users():
  users_list = []
  for user in db.user.find():
    users_list.append(user)
  return dumps(users_list)


@app.route('/user/<int:userid>')
def user(userid):
  return dumps(db.user.find_one({'userid': userid}))
