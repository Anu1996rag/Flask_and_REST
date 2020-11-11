''' Simple hello world script using Flask '''

from flask import Flask,jsonify

# object declaration
app = Flask(__name__)


# this is the default path : http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return 'hello world'

# this will invoke when we use the path : http://127.0.0.1:5000/hithere
@app.route('/hithere')
def hi_there():
    return "I just hit hi there !"

# this will invoke when we use the path : http://127.0.0.1:5000/compute
@app.route('/compute')
def compute():
    c = 2*534
    s = str(c)
    result = {
        'Operands':'2 and 534',
        'Operator':'*',
        'Result':s
    }
    # we will return the result in the json format
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
