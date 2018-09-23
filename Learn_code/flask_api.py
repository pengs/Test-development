#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/23 15:52
# @Author  : dapengchiji！！
# @FileName: flask_api.py

from flask import Flask,url_for,request
from flask import render_template
app = Flask(__name__)

def valid_login(username,password):
    if username=='dapeng'and password=='test123':
        return True
    else:
        return False

@app.route("/login",methods=['POST','GET','PUT','DELETE'])
def login():
    if request.method=='POST':
        if valid_login(request.form['username'],request.form['password']):
            print("login successfully")
            return "登录成功"
    else:
       return "Hello World!"
if __name__=='__main__':
    app.run()
