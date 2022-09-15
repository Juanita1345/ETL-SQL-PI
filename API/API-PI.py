from fastapi import FastAPI
from routes.user import user


app=FastAPI()

app.include_router(user)

@app.get('/')
def read_root():
    return{'Welcome':'This is the API for PI'}
