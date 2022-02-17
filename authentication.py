USER_DATA = {
"masnun": "abc123"
}


class User(object):
    def __init__(self, id):
        self.id = id

def __str__(self):
    return "User(id='%s')" % self.id


def verify(username, password):
    if not (username and password):
        return False
    if USER_DATA.get(username) == password:
        return User(id=123)

def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}