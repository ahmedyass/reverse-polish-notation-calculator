import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate_success():
    response = client.post("/api/calculate", json={"expression": "3 4 +"})
    assert response.status_code == 200
    assert response.json()["result"] == 7

def test_calculate_invalid_expression():
    response = client.post("/api/calculate", json={"expression": "3 4 &"})
    assert response.status_code == 400
    assert "Erreur" in response.json()["detail"]

def test_calculate_division_by_zero():
    response = client.post("/api/calculate", json={"expression": "10 0 /"})
    assert response.status_code == 400
    assert "division par zéro" in response.json()["detail"]

def test_get_history():
    response = client.get("/api/history")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_export_csv():
    response = client.get("/api/export")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
