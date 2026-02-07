def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_register(client):
    response = client.post(
        "/auth/register",
        json={"username": "alice", "email": "alice@example.com", "password": "secret123"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    assert "id" in data
    assert "password" not in data
    assert "hashed_password" not in data


def test_register_duplicate(client):
    client.post(
        "/auth/register",
        json={"username": "alice", "email": "alice@example.com", "password": "secret123"},
    )
    response = client.post(
        "/auth/register",
        json={"username": "alice", "email": "alice@example.com", "password": "secret123"},
    )
    assert response.status_code == 409


def test_login(client):
    client.post(
        "/auth/register",
        json={"username": "alice", "email": "alice@example.com", "password": "secret123"},
    )
    response = client.post(
        "/auth/login",
        data={"username": "alice", "password": "secret123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post(
        "/auth/register",
        json={"username": "alice", "email": "alice@example.com", "password": "secret123"},
    )
    response = client.post(
        "/auth/login",
        data={"username": "alice", "password": "wrongpassword"},
    )
    assert response.status_code == 401


def test_me_authenticated(client):
    client.post(
        "/auth/register",
        json={"username": "alice", "email": "alice@example.com", "password": "secret123"},
    )
    login_response = client.post(
        "/auth/login",
        data={"username": "alice", "password": "secret123"},
    )
    token = login_response.json()["access_token"]
    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"


def test_register_invalid_email(client):
    response = client.post(
        "/auth/register",
        json={"username": "alice", "email": "not-an-email", "password": "secret123"},
    )
    assert response.status_code == 422


def test_me_unauthenticated(client):
    response = client.get("/auth/me")
    assert response.status_code == 401
