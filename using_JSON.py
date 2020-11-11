''' File demonstrates using JSON file format '''


from flask import Flask,jsonify

# object declaration
app = Flask(__name__)

@app.route('/')
def jsonFile():
    retJson = {
        'Name':'Anurag', # string
        'Age':24,           # number
        'Phones':[          # array of objects
            {
                'Primary':456321        # first object
            },
            {
                'phoneName':'Alternate',        # second object
                'phoneNum':123456
            }
        ]
    }

    return jsonify(retJson) # returning in the json format 



if __name__ == "__main__":
    app.run(debug=True)
