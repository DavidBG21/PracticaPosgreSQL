
from orm.config import BaseClass
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
import datetime

class Usuario(BaseClass):
    __tablename__="usuarios"
    id=Column(Integer,primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(100))
    email=Column("email",String(100))
    password=Column(String(40))
    fecha_registro=Column(DateTime(timezone=True), default=datetime.datetime.now)

class Compra(BaseClass):
    __tablename__="compras"
    id=Column(Integer,primary_key=True)
    id_usuario=Column(Integer, ForeignKey(Usuario.id))
    producto=Column(String(100))
    precio=Column(Float)

class Foto(BaseClass):
    __tablename__="fotos"
    id=Column(Integer,primary_key=True)
    id_usuario=Column(Integer, ForeignKey(Usuario.id))
    titulo=Column(String(100))
    descripcion=Column(String(100))
    ruta=Column(String(50))