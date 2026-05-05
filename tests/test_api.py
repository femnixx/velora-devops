from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_create_and_get_item():
    r = client.post("/items/p1", json={"name": "Widget", "price": 9.99})
    assert r.status_code == 200

def test_duplicate_item_rejected():
    client.post("/items/p2", json={"name": "Gadget", "price": 4.99})
    r = client.post("/items/p2", json={"name": "Gadget", "price": 4.99})
    assert r.status_code == 409

def test_not_found():
    r = client.get("/items/doesnotexist")
    assert r.status_code == 404

# Run: pytest tests/ -v