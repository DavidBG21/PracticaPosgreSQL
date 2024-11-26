import orm.modelos as modelos
from sqlalchemy.orm import Session

def usuario_por_id(sesion:Session, id_usuario:int):
    print("select * from app.usuarios where id = ",id_usuario)
    # Devuelve un objeto de tipo Usuario
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

def compra_por_id(sesion:Session, id_usuario:int):
    print("select * from app.compras where id_compra = ",id_usuario)
    # Devuelve un objeto de tipo Compra
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_usuario).first()

def foto_por_id(sesion:Session, id_usuario:int):
    print("select * from app.fotos where id_usuario = ",id_usuario)
    # Devuelve un objeto de tipo Foto
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_usuario).first()
