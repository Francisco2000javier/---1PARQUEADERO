from flask import Flask, render_template 


app=Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/CONTRASEÑA")
def CONTRASEÑA():
  return render_template("CONTRASEÑA.html")

@app.route("/registro")
def registro():
  return render_template("registro.html")
  

@app.route("/SERVICIOS")
def SERVICIOS():
  return render_template("SERVICIOS.html")

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
    app.run(debug=True)
    
    