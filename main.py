from os import environ
from json import loads
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import ORIGINS, ORIGIN_REGEX

app = FastAPI()

app.add_middleware( CORSMiddleware, allow_origins=ORIGINS, allow_origin_regex=ORIGIN_REGEX, allow_credentials=True, allow_methods=['*'], allow_headers=['*'] )

@app.get( '/' )
async def root():
  return { 'message': 'Hello from Iris App FastAPI Back-End' }

@app.get( '/orgs' )
async def get_orgs():
  return ORIGINS

@app.get( '/org_rgx' )
async def get_org_rgx():
  return ORIGIN_REGEX
