''' This file shows the basics of authentication/authorization using Flask '''

from flask import Flask, request, make_response
from functools import wraps

app = Flask(__name__)


# base wrapper function
def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization

        # check if the inputs match
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)

        # if the inputs does not match
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required "'})

    return decorated


# this endpoint for anyone who can see
@app.route('/unprotected')
def unprotected():
    return 'You are in without security'


# this endpoint is for people who are only authorized to see
@app.route('/protected')
@auth_required
def protected():
    return '<h2> you are in </h2>'


# login window
@app.route('/login')
@auth_required
def login():
    return '<h2> you are logged in </h2>'


if __name__ == "__main__":
    app.run(debug=True)
