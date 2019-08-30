from flask import Flask, request, jsonify
import json as simplejson
from bson.json_util import dumps


app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to Python Flask, hello coder!"


@app.route("/login/<string:username>/<string:password>", methods=['GET'])
def login_user(username, password):
    try:
        return dumps ({ 'success':'yes','username':username, 'password': password})
    except Exception as e:
        return dumps({'error' : str(e)})



@app.route("/user-create", methods = ['POST'])
def create_user():
    try:
        # accepts data in the body of the method
        user_name = request.form['username']
        password = request.form['password']
        return dumps ({'success':'yes','username':user_name,'password':password})


    except Exception as e:
        return dumps({'error' : str(e)})



if __name__ == '__main__':
    app.run()