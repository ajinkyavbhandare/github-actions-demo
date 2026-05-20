import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_endpoint():
    """Ensure the root is reachable."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "System Operational"}


def test_compute_endpoint_success():
    """Ensure the computation endpoint processes data correctly."""
    payload = {"n": 100}
    response = client.post("/compute", json=payload)
    assert response.status_code == 200
    assert "result" in response.json()
    # 100 iterations: sum of i^2 for i=0..99 = 328350
    assert response.json()["result"] == 328350


def test_compute_endpoint_default():
    """Ensure it handles default values correctly."""
    response = client.post("/compute", json={})
    assert response.status_code == 200
    assert isinstance(response.json()["result"], int)
