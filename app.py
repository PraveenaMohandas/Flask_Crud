from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:iphone21@localhost/flask_crud'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)
    
@app.route('/add_data', methods=['POST'])
def add_data():
    if request.method == 'POST':
        userid= request.json['userid']
        userid = int(userid)
        username=request.json['username']
        address=request.json['address'] 
        sql = text('INSERT INTO employee ("user_id","user_name","address") VALUES (:userid, :username,:address)')
        sqlexec = db.engine.execute(sql, {'userid':userid, 'username':username, 'address':address})
        msg = "Added data to employee"
        return jsonify({"response": msg})
    
@app.route('/getdata/<id>', methods=['GET'])
def getdata(id):
    if request.method == 'GET':
        userid = id
        sql= text('Select "user_id","user_name","address" from employee WHERE "user_id"=:userid')
        getdata= db.engine.execute(sql, {'userid':userid})
        return jsonify({"response": [dict(row) for row in getdata]})
    
  
@app.route('/updatedata/<id>', methods=['PUT'])
def updatedata(id):
    if request.method == 'PUT':
        userid= id
        username = request.json['username']
        address = request.json['address']
        sql= text('UPDATE employee SET user_name =:username, address=:address WHERE "user_id" =:userid')
        updatedata= db.engine.execute(sql, {'userid':userid,'username':username,'address':address})
        msg="Updated"
        return jsonify({"response": msg})

    
@app.route('/deletedata/<id>', methods=['DELETE'])
def deletedata(id):
  if request.method == 'DELETE':
        userid = id
        deletesql =text('DELETE from employee where "user_id"=:userid')
        deleteexecute = db.engine.execute(deletesql, {'userid':userid})
        msg="Deleted"
        return jsonify({"response": msg})

if __name__ == '__main__':
    app.debug= True
    app.run(debug=True)
