from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():
    client.post(
        "/auth/register",
        json={"email": "aiuser@test.com", "password": "test123"}
    )

    response = client.post(
        "/auth/login",
        json={"email": "aiuser@test.com", "password": "test123"}
    )

    return response.json()["access_token"]


def test_ai_stub_response():
    token = get_token()

    response = client.get(
        "/ai/suggest",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert "daily_plan" in response.json()
    assert isinstance(response.json()["daily_plan"], list)