from app.main import app
from fastapi.testclient import TestClient


client = TestClient( app )


def test_http_root():
  response = client.get( '/' )
  assert response.json() == { 'http_msg': 'Hello from Iris App FastAPI Server' }
  assert response.status_code == 200
