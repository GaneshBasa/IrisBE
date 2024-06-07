from os import environ
from json import loads
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.config import ORIGINS

app = FastAPI()

# app.add_middleware( CORSMiddleware, allow_origins=ORIGINS, allow_credentials=True, allow_methods=['*'], allow_headers=['*'] )

@app.get('/')
async def root():
  return {'message': 'Hello from Iris App FastAPI Back-End'}

@app.get( '/env' )
async def get_env( var_name: str ):
  if var := environ.get( var_name ):
    return loads( var )
  else:
    return var
