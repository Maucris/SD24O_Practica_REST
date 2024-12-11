from pydantic import BaseModel

#Definir esquema alumno

class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera: str
    trimestre: str
    email: str
    password: str
#Definir esquema calificacion
class CalificacionBase(BaseModel):
    uea:str
    calificacion:str
    
#Definir esquema foto
class FotoBase(BaseModel):
    titulo:str
    descripcion:str
    ruta:str
