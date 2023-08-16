#Traer la dependencia - app o .
from . import db
#Traer dependencia
from datetime import datetime

#Crear modelos
class Cliente(db.Model):
    #Definir los atributos
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(128), nullable = True)
    email = db.Column(db.String(120), nullable = True)
    #relaciones SQL alchemy
    ventas = db.relationship('Venta', backref = "cliente", lazy = "dynamic")

class Producto(db.Model):
    #Definir atributos
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key = True) 
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))
    
class Venta(db.Model):
    #Definir atributos
    __tablename__ = "ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    #Clave foránea
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    
    
class Detalle(db.Model):
    #Definir atributos
    __tablename__ = "detalles"
    id = db.Column(db.Integer, primary_key = True)
    #Clave foránea
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)
