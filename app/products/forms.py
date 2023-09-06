#Importar dependencias
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed

#Formulario de registro de nuevo producto
class NewProductForm(FlaskForm):
    nombre = StringField(validators = [ InputRequired(message="El campo nombre esta vacío.") ],
                        label = 'Ingrese nombre:')
    precio = IntegerField(validators=[
                                        InputRequired(
                                            message= "Precio Requerido"),
                                        NumberRange(
                                            message= " Precio fuera de rango", 
                                            min = 1000,
                                            max = 10000
                                        )
                                    ],
                        label = 'Ingrese precio:')
    imagen = FileField(label = 'Cargue imagen del producto:',
                        validators =[
                            FileRequired(
                                message=" Suba una imagen"
                                ),
                            FileAllowed(
                                ["jpg" , "png"], 
                                message="El tipo de archivo es incorrecto"
                            )
                        ])
    submit = SubmitField ('Registrar')