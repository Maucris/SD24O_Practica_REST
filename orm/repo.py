import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

def devuelve_alumnos(sesion: Session):
    print("select * from app.alumnos")
    return sesion.query(modelos.Alumno).all()

def devuelve_fotos(sesion: Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Foto).all()

def devuelve_calificaciones(sesion: Session):
    print("select * from app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

def alumno_por_id(sesion: Session, id_al: int):
    print("select * from app.alumnos where id alumno =", id_al)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_al).first()

def foto_por_id(sesion: Session, id_fo: int):
    print("select * from app.fotos where id foto =", id_fo)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_fo).first()

def calificacion_por_id(sesion: Session, id_cal: int):
    print("select * from app.calificaciones where calificacion id =", id_cal)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_cal).first()

def fotos_por_id_alumno(sesion: Session, id_al: int):
    print("select * from app.fotos where id_alumnos =", id_al)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno == id_al).all()

def calificaciones_por_id_alumno(sesion: Session, id_al: int):
    print("select * from app.calificaciones where id_alumnos =", id_al)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_al).all()

def borrar_calificaciones_por_id_alumno(sesion: Session, id_al: int):
    print("delete from app.calificaciones where id_alumnos =", id_al)
    calificaciones = calificaciones_por_id_alumno(sesion, id_al)
    if calificaciones is not None:
        for calificacion in calificaciones:
            sesion.delete(calificacion)
        sesion.commit()

def borrar_fotos_por_id_alumno(sesion: Session, id_al: int):
    print("delete from app.fotos where id_alumnos =", id_al)
    fotos = fotos_por_id_alumno(sesion, id_al)
    if fotos is not None:
        for foto in fotos:
            sesion.delete(foto)
        sesion.commit()
    

def borrar_alumno_por_id(sesion: Session, id_al: int):
    print("delete from app.alumnos where id =", id_al)
    
    alumno = alumno_por_id(sesion, id_al)
    if alumno is not None:
        sesion.delete(alumno)
        sesion.commit()
    respuesta= {
        "mensaje": "alumno eliminado"
    }
    
    return respuesta