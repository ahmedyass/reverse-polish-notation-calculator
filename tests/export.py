import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_export_no_data(mocker):
    """Test pour exporter un fichier CSV vide si aucune donnée n'est trouvée."""
    mocker.patch("app.crud.get_all_calculations", return_value=[])
    
    response = client.get("/export")
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv"
    assert response.text == "expression,result,created_at\n"  # Seulement les en-têtes
