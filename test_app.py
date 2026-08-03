import pytest

from app import app, obtener_estado_sistema

def test_obtener_estado_sistema():
    assert obtener_estado_sistema(50) == "OK"
    assert obtener_estado_sistema(85) == "ALERTA"
    assert obtener_estado_sistema(80) == "ALERTA"

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ruta_raiz(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"GitOps" in response.data

def test_ruta_status(client):
    response = client.get('/status/40')
    assert response.status_code == 200
    assert response.json == {"cpu_actual ": 40, "estado_sistema": "OK"}