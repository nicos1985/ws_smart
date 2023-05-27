
from peewee import *
import datetime
import ast
import os 


# Crea una instancia de la base de datos con la ruta especificada


# Define el formato de fecha
FORMATO_FECHA = "%d-%m-%Y"
FORMATO_FECHA_HORA = '%d-%m-%Y %H:%M:%S'

# Define el modelo de la tabla
class Galicia_Clients(Model):
    dni = IntegerField()
    nombre = CharField()
    estado = CharField()
    sexo = CharField()
    fecha_nacimiento = DateField(formats=[FORMATO_FECHA])
    monto = IntegerField()
    puesto = CharField()
    fecha_creacion = TextField(default=datetime.datetime.now().strftime(FORMATO_FECHA_HORA))
    fecha_modificacion = TextField(default=datetime.datetime.now().strftime(FORMATO_FECHA_HORA))

    class Meta:
        try:
            with open('parametros.txt', 'r') as leer_param:
                parametros = leer_param.read()
                diccionario = ast.literal_eval(parametros)
            print(diccionario)
            base = diccionario['base_datos']
            print(base)
            ruta_basedatos = f'{base}/smart_bd.db'
            print(f'rutabd_try:{ruta_basedatos}')
        
        except (OperationalError, SyntaxError, KeyError):
            ruta_basedatos = f'{os.getcwd()}/smart_bd.db'
            print(f'ruta bd_ except: {ruta_basedatos}')

        database = SqliteDatabase(ruta_basedatos)  # Asigna la base de datos a utilizar

    def save(self, *args, **kwargs):
        self.fecha_modificacion = datetime.datetime.now().strftime(FORMATO_FECHA_HORA)
        return super(Galicia_Clients, self).save(*args, **kwargs)
    
    

   

class Smart_Log(Model):
    dni_log = IntegerField(null=True,default='')
    puesto = CharField()
    error = CharField()
    fecha_creacion = TextField(default=datetime.datetime.now().strftime(FORMATO_FECHA_HORA))

    
    class Meta:
        try:
            with open('parametros.txt', 'r') as leer_param:
                parametros = leer_param.read()
                diccionario = ast.literal_eval(parametros)
            print(diccionario)
            base = diccionario['base_datos']
            print(base)
            ruta_basedatos = f'{base}/smart_bd.db'
            print(f'rutabd_try:{ruta_basedatos}')
        
        except (OperationalError, SyntaxError, KeyError):
            ruta_basedatos = f'{os.getcwd()}/smart_bd.db'
            print(f'ruta bd_ except: {ruta_basedatos}')

        database = SqliteDatabase(ruta_basedatos)  # Asigna la base de datos a utilizar

    def save(self, *args, **kwargs):
        self.fecha_creacion = datetime.datetime.now().strftime(FORMATO_FECHA_HORA)
        return super(Smart_Log, self).save(*args, **kwargs)
    
    

