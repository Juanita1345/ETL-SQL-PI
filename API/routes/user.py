
from fastapi import APIRouter
from config.Test import answ_1,answ_2,answ_3,df2, answ_4,answ_41
from config.DB_con import conn
import pandas as pd
from pydantic import BaseModel


user=APIRouter()

#Se crea una clase con la estructura para las consultas personalizadas
class query(BaseModel):
    Consulta: str

#Pagina respuesta a pregunta 1
@user.get("/Pregunta_1")
def get_answer():
    return {'Año con mas carreras':answ_1}

#Pagina respuesta a pregunta 2
@user.get("/Pregunta_2")
def get_answer():
    return {'Piloto con mayor cantidad de premios':answ_2}

#Pagina respuesta a pregunta 3
@user.get("/Pregunta_3")
def get_answer():
    return {'Nombre del circuito mas recorrido':answ_3}

#Pagina respuesta a pregunta 4
@user.get("/Pregunta_4")
def get_answer():
    return {'Piloto con mayor cantidad de puntos':answ_4,"Nacionalidad":answ_41}

#Consulta personalizada

Consulta=[]

#Publicacion de consulta
@user.get('/consultas')
def read_consulta():
    return Consulta[-1]


#Ingreso de consulta
@user.post('/post')
def consulta(query:query):
    info=str(query.Consulta)
    #print(info)
    df1=pd.read_sql_query(info, conn)
    info_dic=df1.to_dict()
    Consulta.clear()
    Consulta.append(info_dic)
    return "received"
