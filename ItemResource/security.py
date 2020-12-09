# this file is like database containing users data who has logged in
from user import User
from werkzeug.security import  safe_str_cmp # safe string compares for safer way for comparing strings

users = [
    User(1,"abc","abcd")
]


username_mapping = {u.username:u for u in users}

userid_mapping = {u.id:u for u in users}


# certain methods to authenticate

# to verify using username
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


# to verify from the id
def identity(payload):  # payload = content of the JWT token
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
