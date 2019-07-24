from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps
import os

app = Flask(__name__)
client = MongoClient(host=os.environ['DB_HOST'])
db = client.peopledb

# This is only for the purpose of demo
if db.person.count_documents({}) == 0:
  db.person.insert({'name': 'John'})
  db.person.insert({'name': 'George'})


@app.route('/')
def hello():
  return 'Hello world!'


@app.route('/people')
def people():
  people_list = []
  for person in db.person.find():
    people_list.append(person)
  return dumps(people_list)
