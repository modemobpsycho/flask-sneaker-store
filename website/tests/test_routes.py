from flask import url_for
from website import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Home Page" in response.data


def test_product_page_route(client):
    response = client.get("/product")
    assert response.status_code == 200
    assert b"Product Page" in response.data


def test_home_route_with_data(client):
    with app.app_context():
        # product1 = Product(name="Test Product 1", price=10.0, description = "desc", image_url = "static/images/p1.jpg", category = "sneakers"))
        # db.session.add_all([product1])
        # db.session.commit()

        response = client.get("/")
        assert response.status_code == 200
        assert b"Test Product 1" in response.data
        assert b"Test Product 2" in response.data
        assert b"Size 1" in response.data
        assert b"Size 2" in response.data


if __name__ == "__main__":
    pytest.main()
