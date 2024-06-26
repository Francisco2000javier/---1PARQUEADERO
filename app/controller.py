from flask import Flask, render_template, request,session, redirect, url_for
from flask_mysqldb import MySQL




app=Flask(__name__)
#conexion mysql
from modely import *

#funciones controladores
 #funcio login

@app.route("/login",methods=["POST"])
def add_login():
  if request.method == "POST":
    CORREO =request.form["CORREO"]
    CONTRASEÑA= request.form ["CONTRASEÑA"]
    print(CORREO, CONTRASEÑA)
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT* FROM usuarios WHERE CORREO  = %s  AND CONTRASEÑA = %s", (CORREO,CONTRASEÑA))
    account = cursor.fetchone( )
    if account:
        session["logueado"]= True
         #session["id_rol"] 
          #if session["id_rol"]==1:
        return render_template("INICIO.html")
         #elif session["id_rol"]==2:
         #return "admin"

    else:
         return render_template("index.html", mensaje="usuario incorrecto")
    #fin login 
    
    
    

     #inici registro
@app.route("/add_registro", methods=["POST"])
def add_registro():
  if request.method == "POST":
    CORREO =request.form["CORREO"]
    CONTRASEÑA= request.form ["CONTRASEÑA"]
    PAIS= request.form["PAIS"]
    CONTRASEÑA= request.form["CONTRASEÑA"]
    DIRECCION= request.form["DIRECCION"]
    TELEFONO=request.form["TELEFONO"]
    CORREO= request.form["CORREO"]
    NUMERODEDOCUMENTO=request.form["NUMERODEDOCUMENTO"]
    TIPODEDOCUMENTO= request.form["TIPODEDOCUMENTO"]
 
 
    NOMBRES=request.form["NOMBRES"]
    APELLIDOS = request.form["APELLIDOS"]
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO usuarios (NOMBRES,APELLIDOS,TELEFONO,CORREO,CONTRASEÑA,PAIS,DIRECCION,TIPODEDOCUMENTO,NUMERODEDOCUMENTO,id_rol) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,2)",[NOMBRES,APELLIDOS,TELEFONO,CORREO,CONTRASEÑA,PAIS,DIRECCION,TIPODEDOCUMENTO, NUMERODEDOCUMENTO])
    mysql.connection.commit()
    return render_template("index.html", mensaje2=" registro exitoso")
     
     #fin registro
     
     #CONTROLADORES

@app.route("/")
def index():
   return render_template("index.html")


@app.route("/lista")
def lista():
   return render_template("lista.html")



@app.route("/regi")
def registro():
  return render_template("regi.html")


@app.route("/CONTRASEÑA")
def CONTRASEÑA():
  return render_template("CONTRASEÑA.html")


@app.route("/SERVICIOS")
def SERVICIOS():
  return render_template("SERVICIOS.html")


  

@app.route("/ingreso")
def ingrreso():
  return render_template("ingreso.html")

@app.route("/add_in", methods=["POST"])
def add_in():
  if request.method == "POST":
     PLACA =request.form["PLACA"]
     #MODEL=request.form["MODELO"]
     TIPO= request.form["TIPO"]
     HOR= request.form["HORA"]
     #descripsion = request.form["descripsion"]
     print(PLACA)
     cursor = mysql.connection.cursor()
     cursor.execute(" INSERT INTO rvehiculo (PLACA,TIPOVEHICULO,HORALLEGADA) VALUES (%s,%s,%s)",[PLACA,TIPO,HOR]  )
     mysql.connection.commit()
     return render_template("INICIO.html") 
    
    
    

@app.route("/SALIDA")
def SALID():
  return render_template("SALIDA.html")


@app.route("/TARIFA")
def TARIFA():
  return render_template("TARIFA.html")

@app.route("/CONTACTO")
def CONTACTO():
  return render_template("CONTACTO.html")

@app.route("/ACERCA DE")
def ACERCA_DE():
  return render_template("ACERCA DE.html")

@app.route("/INICIO")
def INICIO():
  return render_template("INICIO.html")


@app.route("/ESTADO")
def ESTADO():
  return render_template("ESTADO.html")


@app.route("/PQRS")
def PQRS():
  return render_template("PQRS.html")


@app.route("/TICKET")
def TICKET():
  return render_template("TICKET.html")


@app.route("/index")
def SALIR():
   return render_template("index.html")
 
 
  



if __name__=="__main__":
    app.secret_key = "pi"
    app.run(debug=True)



    
    