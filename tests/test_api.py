from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello Todo API"
    
def test_get_tasks():
    response = client.get("/tasks/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_create_task():
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Testing API",
            "completed": False
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Task created"
    assert "id" in data