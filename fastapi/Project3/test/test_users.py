from test.utils import *
from routers.todos import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == test_user.username
    assert response.json()["email"] == test_user.email
    assert response.json()["first_name"] == test_user.first_name
    assert response.json()["last_name"] == test_user.last_name
    assert response.json()["role"] == test_user.role
    assert response.json()["phone_number"] == test_user.phone_number
