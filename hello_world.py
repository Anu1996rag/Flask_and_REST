''' Simple hello world script using Flask '''

from flask import Flask

# object declaration
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == "__main__":
    app.run()
