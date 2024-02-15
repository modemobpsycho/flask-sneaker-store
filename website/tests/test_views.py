from website import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Home Page" in response.data


def test_login(client):
    response = client.post(
        "/login",
        data=dict(username="test_user", password="password"),
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Hello, test_user!" in response.data
