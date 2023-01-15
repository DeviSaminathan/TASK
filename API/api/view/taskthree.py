import os
import sys
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent)
from flask import jsonify
from route import app
from model.normal_db import Master_db
dbs = Master_db()

def avg_rating():
    data=dbs.avgmov()
    avg=[]
    for i in data:
        details=dbs.movieavg(i[0])
        avg.append({"genre" : details[4], "runtimeMinutes" : details[3],"primaryTitle" : details[2],"tconst": details[0]})
    return jsonify(avg)
   