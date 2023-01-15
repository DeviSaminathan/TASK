import os
import sys
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent)
from flask import request, jsonify
from route import app
from model.normal_db import Master_db
dbs = Master_db()
        
def addmovie():
    data=request.get_json()
    const=data['tconst']
    ttype=data['titletype']
    ptitle=data['primarytitle']
    runtime=data['runtimeminutes']
    gen=data['genre']
    insert=dbs.insertmovie(const,ttype,ptitle,runtime,gen)
    if insert == 1:
        return jsonify("success")
    else : 
        return jsonify(" error in insering ,tconst may be existing one try with other tconst")
    
       
        
   