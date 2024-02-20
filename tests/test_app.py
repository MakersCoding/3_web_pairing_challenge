from flask import jsonify
def test_example(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200

def test_get_all_users(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200
    assert response.json == [{"id":1,"username":"john"},{"id":2,"username":"jane"},{"id": 3,"username":"alice"}]

def test_get_specific_user(web_client):
    response = web_client.get("/users/1")
    assert response.status_code == 200
    assert response.json == {"id":1,"username":"john"}

def test_get_specific_user_error(web_client):
    response = web_client.get("/users/10")
    assert response.status_code == 404
    assert response.json == {'error': 'User not found'}

def test_post_make_user(web_client):
    response = web_client.post("/users", json={"username": "name"})
    assert response.status_code == 201
    assert response.json == {"id":4,"username":"name"}

def test_post_username_required_error(web_client):
    response = web_client.post("/users", json={}) # <= specify blank json file
    assert response.status_code == 400
    assert response.json == {'error': 'Username is required'}

def test_put_update_user(web_client):
    response = web_client.put("/users/1", json={"username": "name"})
    assert response.status_code == 200
    assert response.json == {"id":1,"username":"name"}

def test_put_update_user_error(web_client):
    response = web_client.put("/users/10")
    assert response.status_code == 404
    assert response.json == {'error': 'User not found'}

def test_put_update_username_error(web_client):
    response = web_client.put("/users/2", json={}) # <= specify blank json file
    assert response.status_code == 400
    assert response.json == {'error': 'Username is required'}

def test_delete_user(web_client):
    response = web_client.delete("/users/1")
    assert response.status_code == 200
    assert response.json == {'message': 'User deleted'}