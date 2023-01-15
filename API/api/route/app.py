import os
import sys
from flask import Flask
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent)
from flask import Flask
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from view.taskone import *
from view.tasktwo import *
from view.taskthree import *
import urllib.parse
app = Flask(__name__)
passworD = urllib.parse.quote_plus("devi")
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:%s@127.0.0.1:3308/onito"% passworD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']="PTZLOPnkjXFIhnfqfv0Bg6JlvK7oLHZQuMV2p2UAnqY="
api = Api(app)
db=SQLAlchemy(app)
Base = automap_base()
Base.prepare(db.engine,reflect=True)


@app.route('/', methods=['GET'])
def welcome():
    return "welcome Onito" 

@app.route('/api/v1/longest-duration-movies', methods=['GET'])
def task1():
    return longduration()


@app.route('/api/v1/new-movie', methods=['POST'])
def task2():
    return addmovie()

@app.route('/api/v1/top-rated-movies', methods=['GET'])
def task3():
    return avg_rating()

if __name__=="__main__":
    app.run(debug=True)