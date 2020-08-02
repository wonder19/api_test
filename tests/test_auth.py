from model.login_auth import UserData


def test_login(unauth_client, get_username, get_password):
    res = unauth_client.auth(UserData(username=get_username, password=get_password))
    assert res.status_code == 200


def test_bad_credentials_password(unauth_client, get_username):
    res = unauth_client.auth(UserData(username=get_username, password=""))
    assert res.status_code == 200
    assert res.json().get("reason") == "Bad credentials"
