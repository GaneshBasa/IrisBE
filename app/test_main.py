from app.main import app
from fastapi.testclient import TestClient


client = TestClient( app )

HOST = 'localhost'
PORT = 8000
WSS_BASE_URL = f'wss://{HOST}:{PORT}'

def ws_helper( relative_url: str ) -> str:
  return WSS_BASE_URL + relative_url


def test_http_root():
  response = client.get( '/' )
  assert response.status_code == 200
  assert response.json() == { 'http_msg': 'Hello from Iris App FastAPI Server' }


def test_ws_root():
  with client.websocket_connect( ws_helper( '/' ) ) as ws:
    data = ws.receive_json()
    assert data == { 'ws_msg': 'Hello from Iris App FastAPI Server' }


def test_ws_test():
  with client.websocket_connect( ws_helper( '/test' ) ) as ws:
    for i in range( 10 ):
      data = ws.receive_json()
      assert data == { 'count': i + 1 }
