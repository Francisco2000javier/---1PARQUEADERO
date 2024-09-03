from flask import Flask, render_template, request, redirect, url_for,session
import mysql
from datetime import datetime


# Crear una instancia de la aplicación Flask
app = Flask(__name__)


#------- IMPORTAR MODELO---
from modelo import *
#-----------------------

 
  
#---INICIO SESSION REGISTRO
#--CONTROLADOR REGISTRO

@app.route("/regi")
def registr():
  return render_template("regi.html")
  
  
#------ Ruta para agregar una nuevo usuario

@app.route("/add_registro", methods=["POST"])
def add_registro():
  
  #--------recoger la informacion  del formulario
  
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
    
  #--Establecer conexión con la base de datos

    connection = get_db_connection()
    cursor = connection.cursor()
    
  #--------- insertar  la informacion  en la tabla usuario
  
    cursor.execute("INSERT INTO usuari (NOMBRES,APELLIDOS,TELEFONO,CORREO,CONTRASEÑA,PAIS,DIRECCION,TIPODOCUMENTO,NUMERODEDOCUMENTO,id_rol) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,2)"
                   ,[NOMBRES,APELLIDOS,TELEFONO,CORREO,CONTRASEÑA,PAIS,DIRECCION,TIPODEDOCUMENTO, NUMERODEDOCUMENTO])
    connection.commit()
    
  #------------Cerrar la conexión con la base de datos
    connection.close()
    
  #-------------Renderizar la plantilla HTML 'index.html' con un mensaje registro exitoso

    return render_template("index.html", mensaje2=" registro exitoso")
  
  
  #----------FIN SESSION REGISTRO-----------








#----------SESSION INICIO

@app.route("/")
def INICI():
   return render_template("index.html")
 
 #--------ruta para la validacion de usuarios---

@app.route("/login",methods=["POST"])
def add_loginn():
  
  #--------recoger la informacion  del formulario

  if request.method == "POST":
    CORREO =request.form["CORREO"]
    CONTRASEÑA= request.form ["CONTRASEÑA"]
    print(CORREO, CONTRASEÑA)
    
   #--Establecer conexión con la base de datos

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    #------validar la informacion desde la tabla usuario
    cursor.execute("SELECT* FROM usuari WHERE CORREO  = %s  AND CONTRASEÑA = %s", (CORREO,CONTRASEÑA))
    
    #----almacenar la consulta en la variable account
    account = cursor.fetchone( )
    
    #----Cerrar la conexión con la base de datos
    cursor.close()
    
    #-----validamos 
    
    if account is  not None:
      session["CORREO"] = CORREO
      session["CONTRASEÑA"] = CONTRASEÑA
    #----
      session['id_rol'] = account['id_rol'] 
      #----
      
      if session['id_rol']==2:
       return render_template("INICIO.html")
      elif session['id_rol']==1:
          return render_template("admin.html")

    else:
         return render_template("index.html", mensaje="usuario incorrecto")
    
    
    #-------------------------FIN SESSION  INICIO----------------------------
    
    
    
    
    
    
    
    

#------------SESION CONTRASEÑA---------------------------


@app.route("/CONTRASEÑA")
def CONTRASEÑA():
  return render_template("CONTRASEÑA.html")

#-----validacion  si el usuario existe

@app.route("/add_contra",methods=["POST"])
def add_contraeña():
  #---- recoger informacion  del formulario
   if request.method == "POST":
     CORREO = request.form["CORREO"]
     
     #--- establecer conexion con la base de datos
     connection = get_db_connection()
     cursor = connection.cursor()
     
     #---realizar una consulta en la base dedatos 
     cursor.execute("SELECT CORREO FROM usuari WHERE CORREO  = %s",[CORREO]) 
     
     #---almacenar la consulta en una variable
     accounts = cursor.fetchone()
     print(accounts)
     
     #---cerrar la conexion base de datos
     cursor.close()
     
     #---validamos si el usuario  esta registrado
     if accounts is  not None:
      session["CORREO"] = CORREO
      #----renderizar la plantilla si el usuario es correcto y alamcenar la variable de la consulta realizada
      return render_template("nueva.html",accounts=accounts )
     #-----en dado caso de que el usuario noi exista renderisar la plantilla CONTRASEÑA
     else:
      return render_template("CONTRASEÑA.html ",mensaje9="usuario no registrado")
    
  
  #--- agregar nueva contraseña---
  
@app.route("/nueva")
def nueva():
  return render_template("nueva.html")

#------ruta para el formulario crear contraseña nueva

@app.route("/NUEVA",methods=["POST"])
def NUEV():
    #---- recoger  la inforormacion  del formulario
      CONTRASEÑA = request.form["NUEVA"]
      COFCONTRASEÑA = request.form["COFNUEVA"]
      cambio = request.form["CAMBIO"]
      print(cambio,"I")
      #----validamos si ambas contraseñas son iguales
      if (CONTRASEÑA==COFCONTRASEÑA):  
            #---establecer conexion a la base de datos
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            #----realizar  la consulta donde se restablece la contraseña del usuario ya validado
            cursor.execute("UPDATE usuari SET CONTRASEÑA = %s WHERE CORREO= %s",(CONTRASEÑA,cambio))
            connection.commit()
            #---cerrar conexion base de datos
            connection.close()
            #--renderizar a la plantilla index
            return render_template("index.html",mensaje13="Cambio de contraseña exitoso!!")
            #---si la contraseña no son iguales renderizar  a la plantilla nueva con un nuevo mensaje
      else:
       return render_template("nueva.html",mensaje11="CONTRASEÑAS NO CONCIDEN")
     
   #-------------------------------------------------------------------------------------------------#
  
  
#--------------------------FIN SESION DE CONTRASEÑA------------------------------------------------#









#---------------------SESSION INICIO-------------------------------------
   
@app.route("/INICIO")
def IICI():
  return render_template("INICIO.html")

#---------------------FIN------------------------------







#----------------LISTAR USUARIO-----------------------------

@app.route("/lista")
def listarr():
  #------conexion mysql-----#
   connection = get_db_connection()
   cursor = connection.cursor()
   #-------consulta mysql------
   cursor.execute(" SELECT * FROM usuari")
   usuari= cursor.fetchall()
   #------cerrar conexion mysql-
   cursor.close()
   return render_template("lista.html", usuari=usuari)
 
 
 
@app.route("/ELIM/<string:id>")
def LISTAELI(id):
 connection = get_db_connection()
 cursor = connection.cursor()
 cursor.execute("DELETE FROM usuari WHERE idCliente = %s",(id,))
 connection.commit()
 connection.close()
 return render_template("lista.html")

 
  #--------------------fin lista de usuario------









#-------INICIO SESSION TARIFA-----------------
 
 #----------Ruta crear tarifa--------
 
@app.route("/CRTARIF")
def CREART():
    return render_template("CRTARIF.html")
  
  #----------ruta del formulario---
  
@app.route("/add_tarifa",methods=["POST"])
def add_tarifaA():
    if request.method == "POST":
     TIPOVICULO = request.form["TIPODEVEHICULO"]
     HORA = request.form["HORA"]
     MES = request.form["MES"]
     #---conexion mysql----
     connection = get_db_connection()
     cursor = connection.cursor()
     cursor.execute(" INSERT INTO tarifa (TIPOVEHICULO,HORA,MES) VALUES (%s,%s,%s)",[TIPOVICULO,HORA,MES]  )
     connection.commit()
     connection.close()
     return render_template("INICIO.html")
   
   
 #---- -----------TARIFA--------
 
@app.route("/TARIFA")
def EST():
  #----conexion mysql-----
   connection = get_db_connection()
   cursor = connection.cursor()
   #-----realizar una consulta mysql
   cursor.execute(" SELECT * FROM tarifa")
   tarifa = cursor.fetchall()
   print(tarifa)
   #-----cerrar conexion  mysql
   cursor.close()
   return render_template("TARIFA.html",tarifa=tarifa)
 
 #-----------ruta eliminar tarifa--------------
@app.route("/delete/<string:idd>")
def de(idd):
 connection = get_db_connection()
 cursor = connection.cursor()
 cursor.execute("DELETE FROM tarifa WHERE idTarifa = %s",[idd])
 connection.commit()
 connection.close()
 return  render_template("INICIO.html")
 
   #----------FIN SESSION  TARIFA--------------
   
   
   
   
   
   
   
   
   
   
   
#------------SESSION SERVICICOS----------
@app.route("/SERVICIOS")
def SERVICIOS():
  return render_template("SERVICIOS.html")
#-------FIN SERVICIOS------------






#------ruta index---
@app.route("/index")
def S():
   return render_template("index.html")  
 

    
  

#------------------SESION CONTACTO----------------
@app.route("/CONTACTO")
def CONTACTO():
  return render_template("CONTACTO.html")


@app.route("/add_contacto",methods=["POST"])
def ddpqrs():
  if request.method == "POST":
     no = request.form["name"]
     tele = request.form["phone"]
     email = request.form["email"]
     mensa= request.form["message"]
     print(no,tele,email,mensa)
     connection = get_db_connection()
     cursor = connection.cursor()
    #-----------insetar a  base de tas mysql---------------
     cursor.execute("INSERT INTO contacto (NOMBRE,TELEFONO,CORREO,MENSAJE) VALUES (%s,%s,%s,%s)", 
                    (no,tele,email,mensa))
     connection.commit()
  
     return render_template("INICIO.html")
#--------------FIN SESION CONTACTO----------------

#-----------------SESION PQRS---------------
@app.route("/PQRS")
def PQRS():
  return render_template("PQRS.html")

@app.route("/add_pqrs",methods=["POST"])
def addpqrs():
  if request.method == "POST":
     nan= request.form["nombre"]
     email = request.form["correo"]
     reclas= request.form["reclamo"]
     print(nan,email,reclas)
     connection = get_db_connection()
     cursor = connection.cursor()
    #-----------insetar a  base de tas mysql---------------
     cursor.execute("INSERT INTO pqrs (NOMBRES,CORREO,RECLAMO) VALUES (%s,%s,%s)", 
                    (nan,email,reclas))
     connection.commit()
  
 
  return render_template("INICIO.html")




#-----------------FIN PQRS----------------


#------------SESSION ACERCA DE---------------
@app.route("/ACERCA DE")
def ACERCA_DE():
  return render_template("ACERCA DE.html")
#---------------FIN SESSION ACERCA DE----------

#------------SESSION ADMIN--------------
@app.route("/admin")
def adm():
  return render_template("admin.html")


@app.route("/PQRS_")
def PQ():
   #-----------conexion mysql---------
   connection = get_db_connection()
   cursor = connection.cursor()
   cursor.execute(" SELECT * FROM detalle_factura")
   PQRS= cursor.fetchall()
   cursor.close()
   return render_template("PQRS_.html",PQRS=PQRS)
 
 
@app.route("/CONTACT_")
def cont():
   #-----------conexion mysql---------
   connection = get_db_connection()
   cursor = connection.cursor()
   cursor.execute(" SELECT * FROM contacto")
   CONT= cursor.fetchall()
   cursor.close()
   return render_template("CONTACT_.html",CONT=CONT)
 
 
#------------FIN SESSION ADMIN----------+











#--------------SESSION  FACTURA------------

#------ruta ingreso -------------

#-----------Ruta id cliente--------


@app.route('/INGRESO', methods=['GET'])
def home():
   
    # Establecer conexión con la base de datos
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Consulta para obtener la lista de usuarios
    cursor.execute("SELECT concat(NOMBRES, ' ', APELLIDOS) as nombreCompleto, idCliente FROM usuari ")
    users = cursor.fetchall()
    cursor.execute

    # Cerrar la conexión con la base de datos
    connection.close()

    # Renderizar la plantilla HTML 'index.html' con la lista de usuarios
    return render_template('INGRESO.html', users=users) 

@app.route('/id', methods=['GET']) 
def ho():
    # Establecer conexión con la base de datos
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Consulta para obtener la lista de usuarios
    cursor.execute("SELECT concat(TIPOVEHICULO, ' ', HORA) as TIPOVEHICULO, idTarifa FROM tarifa")
    tarif = cursor.fetchall()
    cursor.execute

    # Cerrar la conexión con la base de datos
    connection.close()

    # Renderizar la plantilla HTML 'index.html' con la lista de usuarios
    return render_template('id.html', tarif =tarif) 
  

  
#---------------------------------------------------------


#--------------ruta del formulario ingreso-----------
@app.route("/add_in", methods=["POST"])
def add_in():
   if request.method == "POST": 
     idCliente = request.form["idCliente"]
     PLACA =request.form["PLACA"]
     TIPO= request.form["TIPO"]
     d = datetime.now()
     HOR= d.strftime("%Y-%m-%d %H:%M:%S")
     DES = request.form["descripsion"]
     #-----conexion mysql-----------
     connection = get_db_connection()
     cursor = connection.cursor()
     #-----consulta mysql
     cursor.execute(" INSERT INTO factura (idCliente,PLACA,TIPOVEHICULO,HORALLEGADA,DESCRIPSION) VALUES (%s,%s,%s,%s,%s)",[idCliente,PLACA,TIPO,HOR, DES]  )
     connection.commit()
     
     
     cursor.execute(" SELECT idCliente FROM usuari WHERE idCliente = %s", [idCliente])
     client= cursor.fetchall()
     client = client[(0)]
     print(client[(0)])
    
     # Cerrar la conexión con la base de datos
     connection.close()
     return render_template("INICIO.html",client=client[(0)]) 
   
#------------ruta ticket llegada--------------------

#-------------controlador--------

@app.route("/INGRESO")
def INGRESOOO():
  return render_template("INGRESO.html")
#--------------------------

@app.route("/tikl")
def Tikl():
  #----------conexion---------
   connection = get_db_connection()
   cursor = connection.cursor()
   #---------consulta------------
   cursor.execute(" SELECT * FROM factura ")
   tickl= cursor.fetchall()
   cursor.close()
   return render_template("tikl.html", tickl=tickl)

#--------------SALIDA DEL VEHICULO----------------

#---- Ruta para agregar una nueva factura
@app.route("/tiks")
def Tiks():
  #----------conexion---------
   connection = get_db_connection()
   cursor = connection.cursor()
   #---------consulta------------
   cursor.execute(" SELECT * FROM factura")
   tickl= cursor.fetchall()
   cursor.close()
   return render_template("tiks.html",tickl=tickl)
  #----------------------------------------
  
  #------------ruta retirar vehiculo----------------
@app.route("/factura/<string:id_factura>")
def d(id_factura):
  print(id_factura)
  id_factura = id_factura
  return render_template("factura.html",id_factura=id_factura)
#-------------------...-----------------------------
  
#-----------------ruta obtenr id y cantidad de horas---------------
@app.route("/pago",methods=["POST"])
def ww():
    id_factura = request.form['id_factura']
    print(id_factura)
    CANTIDAD =request.form["CANTIDAD"]
    print(CANTIDAD,"rsc")
    S = datetime.now()
    FECHA = S.strftime("%Y-%m-%d %H:%M:%S")
    print(FECHA)
    #-----------conexion mysql---------------
    connection = get_db_connection()
    cursor = connection.cursor()
    #-----------insetar a  base de tas mysql---------------
    cursor.execute("INSERT INTO entrada (id_factura,HORASALIDA,CANTIDADHORAS,PRECIO) VALUES (%s,%s,%s,5000)", (id_factura,FECHA,CANTIDAD))
    connection.commit()
    #-------------consulta mysql---------
    cursor.execute(" SELECT CANTIDADHORAS FROM entrada WHERE id_factura = %s", (id_factura,))
    CANTIDAD= cursor.fetchall()
    CANTIDAD = CANTIDAD[(0)]
    
    cursor.execute(" SELECT PRECIO FROM entrada WHERE id_factura = %s", (id_factura,))
    PRECIO= cursor.fetchall()
    PRECIO = PRECIO[(0)]
    
    cursor.execute(" SELECT horasalida FROM entrada WHERE id_factura = %s", (id_factura,))
    horas= cursor.fetchall()
    horas = horas[(0)]
    
    cursor.execute(" SELECT CANTIDADHORAS * PRECIO FROM entrada WHERE id_factura = %s", (id_factura,))
    VALOR= cursor.fetchall()
    VALOR  = VALOR[(0)]
    
    
    return render_template("pago.html",id_factura=id_factura,VALOR=VALOR[(0)],CANTIDAD=CANTIDAD[(0)],PRECIO = PRECIO[(0)],horas=horas[(0)])
     


@app.route("/INICIO",methods=["POST"])
def addpag():
  if request.method == "POST":
     id = request.form["id"]
     horas = request.form["horas"]
     CANTI = request.form["CANTIDAD"]
     PREC = request.form["PRECIO"]
     valor = request.form["VALOR"]
     connection = get_db_connection()
     cursor = connection.cursor()
    #-----------insetar a  base de tas mysql---------------
     cursor.execute("INSERT INTO detalle_factura (id_factura,HORASALIDA,CANTIDADHORAS,PRECIO,TOTALPAGAR) VALUES (%s,%s,%s,%s,%s)"
                    , [id,horas,CANTI,PREC,valor])
     connection.commit()
 
     
     return render_template("INICIO.html")
   
    
   #-------------------------------------------------------
   
   #------------ruta detalle factura--------
@app.route("/detall")
def detall():
   #-----------conexion mysql---------
   connection = get_db_connection()
   cursor = connection.cursor()
   cursor.execute(" SELECT * FROM detalle_factura")
   detalle= cursor.fetchall()
   cursor.close()
   return render_template("detall.html",detalle=detalle)
 
@app.route("/INFO")
def INFO():
  
   #-----------conexion mysql---------
   connection = get_db_connection()
   cursor = connection.cursor()
   cursor.execute(" SELECT * FROM factura INNER JOIN detalle_factura ")
   INFO= cursor.fetchall()
   print(INFO)
   cursor.close()
   return render_template("INFO.html",INFO=INFO)
 
 
 
 #-----------FIN TARIFA-------------
 
 #--------------------------------------------------------------------#











if __name__=="__main__":
      app.secret_key = "p#234567in"
      app.run(debug=True)


















