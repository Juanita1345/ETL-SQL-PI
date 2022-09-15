from fastapi import FastAPI
from routes.user import user

#Se crea la aplicacion
app=FastAPI()

#Se llama a el archivo con las rutas
app.include_router(user)

#Mensaje de bienvenida 
@app.get('/')
def read_root():
    return{'Welcome':'This is the API for PI'}
