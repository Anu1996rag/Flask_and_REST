''' This file covers the basics of Authentication/Authorization using JSON Web Tokens (JWT)'''

from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecretkey'


# creating decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')  # http://127.0.0.1/route?token=ftyahscbzn323rfe

        # if the token is not present
        if not token:
            return jsonify({"Message": "Token is not found for current user."}), 403

        # if the token is present , decode it
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:  # if the token is invalid
            return jsonify({"Message": "Token is invalid"}), 403

        return f(*args, **kwargs)

    return decorated


# unprotected endpoint
@app.route('/unprotected')
def unprotected():
    return 'Anyone can see this...'


# protected
@app.route('/protected')
@token_required
def protected():
    return 'this is secured.'


@app.route('/login')
def login():
    auth = request.authorization

    # here the token is generated based on username and the token is valid for only 15 seconds
    if auth and auth.password == 'pass':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=15)},
                           app.config['SECRET_KEY'])

        # return the token in JSON object
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify !', 401, {'WWW-Authenticate': 'Basic realm = "Login Required "'})


if __name__ == "__main__":
    app.run()
