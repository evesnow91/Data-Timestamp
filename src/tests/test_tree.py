def test_responds(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

def test_consistency(test_app):
    """demonstrate that the service can prove a new merkle root has a specific anscestor"""
    response = test_app.get("/ping")