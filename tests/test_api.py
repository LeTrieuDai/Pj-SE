import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:

        response = await client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello Todo API"


@pytest.mark.anyio
async def test_get_tasks():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:

        response = await client.get("/tasks/")

    assert response.status_code == 200


@pytest.mark.anyio
async def test_create_task():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:

        response = await client.post(
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
    