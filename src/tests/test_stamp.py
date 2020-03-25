def test_create_stamp(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

def test_reject_bad_hash(test_app):
    pass

def test_valid_proof(test_app):
    pass

def test_proof_upgrade(test_app):
    pass