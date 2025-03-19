def test_register_user(client):
    """Test user registration."""
    response = client.post("/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepass"
    })
    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully"

def test_register_duplicate_user(client):
    """Test registering with an existing username."""
    client.post("/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepass"
    })

    response = client.post("/register", json={
        "username": "testuser",
        "email": "another@example.com",
        "password": "securepass"
    })
    assert response.status_code == 400
    assert "Username already exists" in response.json["error"]

def test_register_missing_fields(client):
    """Test registration with missing fields."""
    response = client.post("/register", json={})
    assert response.status_code == 400
    assert "Missing username or password" in response.json["error"]
