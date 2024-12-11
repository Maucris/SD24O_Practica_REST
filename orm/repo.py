import orm.modelos as modelos
import orm.esquemas as esquemas 
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


def guardar_alumno(sesion: Session, alumno_nuevo: esquemas.AlumnoBase):
    alumno_bd = modelos.Alumno()

    alumno_bd.nombre = alumno_nuevo.nombre
    alumno_bd.edad = alumno_nuevo.edad
    alumno_bd.domicilio = alumno_nuevo.domicilio
    alumno_bd.carrera = alumno_nuevo.carrera
    alumno_bd.trimestre = alumno_nuevo.trimestre
    alumno_bd.email = alumno_nuevo.email
    alumno_bd.password = alumno_nuevo.password

    sesion.add(alumno_bd)
    sesion.commit()
    sesion.refresh(alumno_bd)
    return alumno_bd

def actualiza_alumno(sesion: Session, id_al: int, alumno_esquema: esquemas.AlumnoBase):
    # Buscar el alumno en la base de datos por su ID
    alumno_bd = alumno_por_id(sesion, id_al)
    if alumno_bd is not None:
        # Actualizar los datos del alumno con los nuevos valores
        alumno_bd.nombre = alumno_esquema.nombre
        alumno_bd.edad = alumno_esquema.edad
        alumno_bd.domicilio = alumno_esquema.domicilio
        alumno_bd.carrera = alumno_esquema.carrera
        alumno_bd.trimestre = alumno_esquema.trimestre
        alumno_bd.email = alumno_esquema.email
        alumno_bd.password = alumno_esquema.password

        # Confirmar los cambios en la base de datos
        sesion.commit()
        sesion.refresh(alumno_bd)  # Refrescar el estado del objeto
        return alumno_bd
    else:
        return {"mensaje": "No se encontró el alumno con el ID especificado"}

def guardar_calificacion(sesion: Session, id_al: int, calificacion: esquemas.CalificacionBase):
    alumno = alumno_por_id(sesion, id_al)
    if alumno is not None:
        calificacion_bd = modelos.Calificacion()
        calificacion_bd.id_alumno = id_al
        calificacion_bd.uea = calificacion.uea
        calificacion_bd.calificacion = calificacion.calificacion
        sesion.add(calificacion_bd)
        sesion.commit()
        sesion.refresh(calificacion_bd)
        return calificacion_bd
    else:
        return {"mensaje": "No se encontró el alumno"}

def actualizar_calificacion(sesion: Session, id_cal: int, calificacion: esquemas.CalificacionBase):
    calificacion_bd = calificacion_por_id(sesion, id_cal)
    if calificacion_bd is not None:
        calificacion_bd.uea = calificacion.uea
        calificacion_bd.calificacion = calificacion.calificacion
        sesion.commit()
        sesion.refresh(calificacion_bd)
        return calificacion_bd
    else:
        return {"mensaje": "No se encontró la calificación"}

def guardar_foto(sesion: Session, id_al: int, foto: esquemas.FotoBase):
    alumno = alumno_por_id(sesion, id_al)
    if alumno is not None:
        foto_bd = modelos.Foto()
        foto_bd.id_alumno = id_al
        foto_bd.titulo = foto.titulo
        foto_bd.descripcion = foto.descripcion
        foto_bd.ruta = foto.ruta
        sesion.add(foto_bd)
        sesion.commit()
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        return {"mensaje": "No se encontró el alumno"}

def actualizar_foto(sesion: Session, id_foto: int, foto: esquemas.FotoBase):
    foto_bd = foto_por_id(sesion, id_foto)
    if foto_bd is not None:
        foto_bd.titulo = foto.titulo
        foto_bd.descripcion = foto.descripcion
        foto_bd.ruta = foto.ruta
        sesion.commit()
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        return {"mensaje": "No se encontró la foto"}