from fastapi.testclient import TestClient
from backend.youtubeapi.start import app  # substitua 'your_fastapi_module' pelo nome do módulo onde está sua aplicação FastAPI

client = TestClient(app)

def test_get_data_returns_status_code_200():
    response = client.get("/get_data")
    assert response.status_code == 200

def test_get_data_returns_multiple_items():
    response = client.get("/get_data")
    data = response.json()
    assert len(data) > 1

