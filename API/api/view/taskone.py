import os
import sys
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent)
from flask import jsonify
from route import app
from model.normal_db import Master_db
dbs = Master_db()

def longduration():
    fetch=dbs.longdur()
    topten=[]
    for i in fetch:
        topten.append({"genre" : i[4],"runtimeMinutes" : i[3], "primaryTitle" : i[2],"tconst": i[0]})
    return jsonify(topten)
   
       
        
   