from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)


# Replace 'localhost' with the MongoDB container name
client = MongoClient("mongodb://flask-mongodb:27017/")
db = client["mydatabase"]


visits_collection = db['visits']

@app.route('/')
def index():
    visit = visits_collection.find_one({'_id': 'visit_count'})
    if not visit:
        visits_collection.insert_one({'_id': 'visit_count', 'count': 0})
        visit = {'count': 0}

    visits_collection.update_one({'_id': 'visit_count'}, {'$inc': {'count': 1}})
    return f'Hello! This page has been visited {visit["count"] + 1} times.'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
