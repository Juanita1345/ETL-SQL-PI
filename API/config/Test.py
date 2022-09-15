import pandas as pd
import numpy as np

from config.DB_con import conn

#Año con más carreras

#Se hace la consulta sobre a tabla Races para saber cuantas carreras se hicieron por año

query_1=("SELECT Year, COUNT(*) as Conteo "
	    "FROM races "
	    "GROUP BY Year")
df1=pd.read_sql_query(query_1, conn)

answ_1=int(df1[(df1['Conteo']==df1['Conteo'].max())].reset_index().loc[0,['Year']])


#Piloto con mayor cantidad de primeros puestos

query_2=("SELECT Driver_id, Forename, Surname, COUNT(*) as Conteo FROM "
        "(SELECT r.Driver_id, Forename, Surname "
        "FROM results r JOIN drivers d ON r.Driver_id=d.Driver_id WHERE Positionorder=1) as drivers_1 "
        "GROUP BY Driver_id")

df2=pd.read_sql_query(query_2, conn)

answ_2=str(df2.loc[0,'Forename'])+" "+str(df2.loc[0,'Surname'])

#Nombre del circuito mas recorrido
query_3=("SELECT c.Name, count(*) as Conteo "
        "FROM races r "
        "JOIN circuits c ON r.circuit_id=c.circuit_id "
        "GROUP BY r.circuit_id "
        "ORDER BY Conteo desc")
df3=pd.read_sql_query(query_3, conn)

answ_3=str(df3.loc[0,'Name'])

#Piloto con mayor cantidad de puntos cuyo constructor sea American o British

query_4=("SELECT r.Driver_id, d.Forename, d.Surname, c.Nationality, SUM(r.Points) as Suma_Puntos FROM "
        "results r JOIN constructors c ON r.Constructor_id=c.constructor_id AND "
        "(Nationality='American' OR Nationality='British') "
        "JOIN drivers d ON r.Driver_id=d.driver_id "
        "GROUP BY r.driver_id")
df4=pd.read_sql_query(query_4, conn)

answ_4=str(df4.loc[0,'Forename'])+" "+str(df4.loc[0,'Surname'])
answ_41=str(df4.loc[0,'Nationality'])