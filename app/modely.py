from flask import Flask, render_template 
from flask_mysqldb import MySQL


app=Flask(__name__)
app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"]= "Robot11"
app.config["MYSQL_DB"]= "parqueadero__p__"
mysql = MySQL(app)





  
        

        
