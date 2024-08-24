from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from app.config import ORIGINS, ALLOWED_HOSTS


app = FastAPI()


app.add_middleware( HTTPSRedirectMiddleware )

app.add_middleware( GZipMiddleware, compresslevel=5 )

app.add_middleware( TrustedHostMiddleware, allowed_hosts=ALLOWED_HOSTS )

app.add_middleware(
  CORSMiddleware,
  allow_origins=ORIGINS,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)


@app.get( '/' )
async def http_root():
  return { 'http_msg': 'Hello from Iris App FastAPI Server' }
