from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from app.config import ORIGINS, ORIGIN_REGEX

app = FastAPI()

app.add_middleware( HTTPSRedirectMiddleware )
app.add_middleware(
  CORSMiddleware,
  allow_origins=ORIGINS,
  allow_origin_regex=ORIGIN_REGEX,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

@app.get( '/' )
async def root():
  return { 'message': 'Hello from Iris App FastAPI Server' }
