#El engine permite confirgurar la conexión a la BD
from sqlalchemy import create_engine
#El session maker permite crear sesiones para hacer consultas
#Por cada consulta se abre y cierra una sesión
from sqlalchemy.orm import sessionmaker
# declarative_base permite definir la clase base para mapear las tablas de la BD
from sqlalchemy.ext.declarative import declarative_base

# EL ESQUEMA SIRVE PARA FRAGMENTAR LA BASE DE DATOS, 
# CUANDO ALGUIEN SE CONECTE A LA BASE DE DATOS SOLO SE PUEDE CONECTAR A CIERTA PARTE DE LA BASE DE DATOS
# CONTROLAR EL ACCESO A LAS TABLAS QUE TIENE

#1. Configurar la conexion BD
# Crear la URL de la BD -> servidorBD://usuario:password@url:puerto/nombreBD
URL_BASE_DATOS = "postgresql://david:david@localhost:5432/ejemplodb"
# Conectarnos mediante el esquema app
engine = create_engine(URL_BASE_DATOS,
                       connect_args={
                           "options": "-csearch_path=app"                           
                       })

#2. Obtener la clase que nos permite crear objetos tipo session
SessionClass = sessionmaker(engine) 
# Crear una función para obtener objetos de la clase SessionClass
def generador_sesion():
    sesion = SessionClass()
    try:
        #equivalente a return sesion pero de manera segura
        yield sesion 
    finally:
        sesion.close()

#3.- Obtener la clase base para mapear tablas
BaseClass = declarative_base()
