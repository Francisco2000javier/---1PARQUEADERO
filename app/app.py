from flask import Flask, render_template, request,session, redirect, url_for
from flask_mysqldb import MySQL


app=Flask(__name__)
#controladores

from controller import *


 
if __name__=="__main__":
  
    app.secret_key = "pin"
    app.run(debug=True)
    
    