from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_success():
    # First register a user
    client.post(
        "/auth/register",
        json={"email": "testuser@test.com", "password": "test123"}
    )

    # Then login
    response = client.post(
        "/auth/login",
        json={"email": "testuser@test.com", "password": "test123"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()