
from peewee import *
import datetime
import ast 

# Define la ruta de la base de datos
with open('parametros.txt', 'r') as leer_param:
    parametros = leer_param.read()
    diccionario = ast.literal_eval(parametros)
print(diccionario)
base = diccionario['base_datos']
print(base)
ruta_basedatos = f'{base}/smart_bd.db'
print(ruta_basedatos)

# Crea una instancia de la base de datos con la ruta especificada
db = SqliteDatabase(ruta_basedatos)

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
        database = db  # Asigna la base de datos a utilizar

    def save(self, *args, **kwargs):
        self.fecha_modificacion = datetime.datetime.now().strftime(FORMATO_FECHA_HORA)
        return super(Galicia_Clients, self).save(*args, **kwargs)

class Smart_Log(Model):
    dni_log = IntegerField(null=True,default='')
    puesto = CharField()
    error = CharField()
    fecha_creacion = TextField(default=datetime.datetime.now().strftime(FORMATO_FECHA_HORA))

    class Meta:
        database = db  # Asigna la base de datos a utilizar

    def save(self, *args, **kwargs):
        self.fecha_creacion = datetime.datetime.now().strftime(FORMATO_FECHA_HORA)
        return super(Smart_Log, self).save(*args, **kwargs)

# Comprueba si la tabla existe antes de crearla

if not Galicia_Clients.table_exists():
    db.create_tables([Galicia_Clients])
    db.close()
if not Smart_Log.table_exists():
    
    db.create_tables([Smart_Log])
    db.close()


"""
from peewee import *
from datetime import datetime

mysql_db = MySQLDatabase(database='previ', user ='smart', host = '192.172.13.40', port = 8991, password = 'Holacarolas')

class Client(Model):
    "A base model that will use our MySQL database"
    nombre = CharField(max_length = 100)
    estado = CharField(max_length=40)
    sexo = CharField(max_length=60)
    fecha_nac = DateField(formats='%d-%m-%Y')
    dni = IntegerField()
    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())

    class Meta:
        database = mysql_db
        #db_table = 'Client'

mysql_db.connect()

query1 = 'SELECT * FROM tables'
mysql_db.execute(query1)
mysql_db.commit()

import mysql.connector

con = mysql.connector.connect(user = 'root', password = 'password', host = '172.18.0.9', port = 8991, database = 'previ')
cursor = con.cursor()

cursor.execute('SELECT * FROM tables')
con.close()
"""