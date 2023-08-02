#Dependencia de flask
from flask import Flask

#Dependencia de modelos
from flask_sqlalchemy import SQLAlchemy

#Dependencia de las migraciones
from flask_migrate import Migrate

#Dependencia para fecha y hora
from datetime import datetime

#Crear el objeto Flask
app = Flask(__name__)

#Definir la "cadena de conexión" (ConnectionString)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3307/flask_shopy_2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

#Crear el objeto de modelos
db = SQLAlchemy(app)

#Crear el objeto de migración
migrate = Migrate(app, db)

#Crear modelos
class cliente(db.Model):
    #Definir los atributos
    __tablename__ = "Clientes"
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(128), nullable = True)
    email = db.Column(db.String(120), nullable = True)

class producto(db.Model):
    #Definir atributos
    __tablename__ = "Productos"
    id = db.Column(db.Integer, primary_key = True) 
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))
    
class ventas(db.Model):
    #Definir atributos
    __tablename__ = "Ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    #Clave foránea
    cliente_id = db.Column(db.Integer, db.ForeignKey('Clientes.id'))
    
class Detalle(db.Model):
    #Definir atributos
    __tablename__ = "Detalles"
    id = db.Column(db.Integer, primary_key = True)
    #Clave foránea
    producto_id = db.Column(db.Integer, db.ForeignKey('Productos.id'))
    venta_id = db.Column(db.Integer, db.ForeignKey('Ventas.id'))
    cantidad = db.Column(db.Integer)
    