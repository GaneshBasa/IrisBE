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

@app.get( '/env_str' )
async def get_env_str( var_name: str ):
  return environ.get( var_name )

@app.get( '/env_json' )
async def get_env_json( var_name: str ):
  return loads( environ.get( var_name ) )
