import app

def test_home():
    client = app.app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    data = r.get_json()
    assert data["status"] == "ok"

def test_health():
    client = app.app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    data = r.get_json()
    assert data["status"] == "healthy"
