from flask import Flask, render_template, request, redirect, url_for,session
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Robot11',
    'database': 'parqueadero__p__'
    # Función para obtener una conexión a la base de datos


}

def get_db_connection():
  return mysql.connector.connect(**db_config)