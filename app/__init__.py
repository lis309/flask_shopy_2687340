#Dependencia de flask
from flask import Flask

#dependencia de configuracion
from .config  import Config

#Dependencia de modelos
from flask_sqlalchemy import SQLAlchemy

#Dependencia de las migraciones
from flask_migrate import Migrate

#Traer la dependencia blueprint
from .mi_blueprint import mi_blueprint
from app.products import products

#Dependencia a bootstrap
from flask_bootstrap import Bootstrap

#Crear el objeto Flask
app = Flask(__name__)

#configuracion del objeto flask
app.config.from_object(Config)

#Vincular blueprint del proyecto
app.register_blueprint(mi_blueprint)
app.register_blueprint(products)

#Crear el objeto de modelos
db = SQLAlchemy(app)

#Crear el objeto de migración
migrate = Migrate(app, db)

#Crear objeto de bootstrap
bootstrap = Bootstrap(app)

#Importar los modelos de models
from .models import Cliente, Producto, Venta, Detalle

