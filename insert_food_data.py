import yaml
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'secret'

# app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/test'
app.config['MONGO_CONNECT'] = True
with open('application.yml') as f:
    info = yaml.load(f, Loader=yaml.FullLoader)
    username = info['username']
    password = info['password']
    app.config['MONGO_URI'] = f'mongodb+srv://{username}:{password}@apptracker.goffn.mongodb.net/calorieApp?retryWrites=true&w=majority'
mongo = PyMongo(app)

f = open('food_data/calories.csv', 'r', encoding = "ISO-8859-1")
l = f.readlines()

for i in range(1, len(l)):
    l[i] = l[i][1:len(l[i]) - 2]

for i in range(1, len(l)):
    temp = l[i].split(",")
    mongo.db.food.insert({'food': temp[0], 'calories': temp[1]})
