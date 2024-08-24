from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from asyncio import sleep

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


@app.websocket( '/' )
async def ws_root( ws: WebSocket ):
  try:
    await ws.accept()
    await ws.send_json( { 'ws_msg': 'Hello from Iris App FastAPI Server' } )
    await ws.close()
  
  except WebSocketDisconnect:
    pass


@app.websocket( '/test' )
async def test( ws: WebSocket ):
  try:
    await ws.accept()
    
    for i in range( 10 ):
      await ws.send_json( { 'count': i + 1 } )
      await sleep( 1 )
    
    await ws.close()
  
  except WebSocketDisconnect:
    pass
