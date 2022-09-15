
from fastapi import APIRouter
from config.Test import answ_1,answ_2,answ_3,df2, answ_4,answ_41

query_table=df2.to_dict()

user=APIRouter()

@user.get("/Pregunta_1")
def get_answer():
    return {'Año con mas carreras':answ_1}

@user.get("/Pregunta_2")
def get_answer():
    return {'Piloto con mayor cantidad de premios':answ_2}

@user.get("/Pregunta_3")
def get_answer():
    return {'Nombre del circuito mas recorrido':answ_3}

@user.get("/Pregunta_4")
def get_answer():
    return {'Piloto con mayor cantidad de puntos':answ_4,"Nacionalidad":answ_41}

@user.get("/Consulta")
def consulta():
    return query_table
