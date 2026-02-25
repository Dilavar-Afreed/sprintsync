from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():
    client.post(
        "/auth/register",
        json={"email": "taskuser@test.com", "password": "test123"}
    )

    response = client.post(
        "/auth/login",
        json={"email": "taskuser@test.com", "password": "test123"}
    )

    return response.json()["access_token"]


def test_create_task():
    token = get_token()

    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Testing task creation"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"