from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo 
from sqlalchemy.orm import Session
from orm.config import generador_sesion 

app = FastAPI()

@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta

@app.get("/alumnos")
def lista_alumnos(sesion: Session = Depends(generador_sesion)):
    print("API consultando todos los alumnos")
    return repo.devuelve_alumnos(sesion)

@app.get("/alumnos/{id}")
def alumno_por_id(id: int, sesion: Session = Depends(generador_sesion)):
    print("API consultando alumno por id =", id)
    return repo.alumno_por_id(sesion, id)



@app.get("/fotos")
def lista_fotos(sesion: Session = Depends(generador_sesion)):
    print("API consultando todas las fotos")
    return repo.devuelve_fotos(sesion)

@app.get("/fotos/{id}")
def foto_por_id(id: int, sesion: Session = Depends(generador_sesion)):
    print("API consultando foto por id =", id)
    return repo.foto_por_id(sesion, id)

@app.get("/alumnos/{id}/fotos")
def fotos_por_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("API consultando fotos del alumno con id =", id)
    return repo.fotos_por_id_alumno(sesion, id)

@app.get("/calificaciones")
def lista_calificaciones(sesion: Session = Depends(generador_sesion)):
    print("API consultando todas las calificaciones")
    return repo.devuelve_calificaciones(sesion)

@app.get("/calificaciones/{id}")
def calificacion_por_id(id: int, sesion: Session = Depends(generador_sesion)):
    print("API consultando calificación por id =", id)
    return repo.calificacion_por_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("API consultando calificaciones del alumno con id =", id)
    return repo.calificaciones_por_id_alumno(sesion, id)


@app.delete("/alumnos/{id}/calificaciones")
def borra_calificaciones_por_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("API eliminando calificaciones del alumno con id =", id)
    repo.borrar_calificaciones_por_id_alumno(sesion, id)
    return {"calificacion borrada", "ok"}

@app.delete("/alumnos/{id}/fotos")
def borra_fotos_por_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("API eliminando fotos del alumno con id =", id)
    repo.borrar_fotos_por_id_alumno(sesion, id)
    return {"fotos borradas", "ok"}

@app.delete("/alumnos/{id}")
def borra_alumno_por_id(id: int, sesion: Session = Depends(generador_sesion)):
    print("API eliminando alumno con id =", id)
    repo.borrar_fotos_por_id_alumno
    repo.borrar_calificaciones_por_id_alumno
    repo.borrar_alumno_por_id
    return {"usuario borado", "ok"}