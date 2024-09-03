from flask import Flask, render_template, request, redirect, url_for,session
import mysql.connector


# Crear una instancia de la aplicación Flask
app = Flask(__name__)
from controller import *


if __name__=="__main__":
    app.secret_key = "p#234567in"
    app.run(debug=True)


















