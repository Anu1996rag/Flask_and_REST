# importing relevant libraries

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# declaring object

app = Flask(__name__)
api = Api(app)


# function to validate the input data
def validateInputData(inputData,functionName):
    if (functionName == "add" or functionName == "subtract" or functionName == "multiply") :
        if ("x" not in inputData) or ("y" not in inputData):
            return 301
        else:
            return 200
    elif functionName == "divide":
        if ("x" not in inputData) or ("y" not in inputData):
            return 301
        elif int(inputData["y"]) == 0:
            return 302
        else:
            return 200



# Addition of Resources
class Add(Resource):  # inheriting Resource class
    def post(self):  # if am here , then Resource Add was requested using method POST
        # step 1 : get the posted data
        inputData = request.get_json()

        # validate the input data
        status_code = validateInputData(inputData,"add")

        if (status_code != 200):
            retJson = {
                "Error Description": "One of the parameters is missing.",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # if the parameters are given
        x = inputData["x"]
        y = inputData["y"]

        # step 2 : converting into integer values
        x = int(x)
        y = int(y)

        # step 3 :addition logic
        sum = x + y

        #  step 4 :convert into json format
        retSum = {
            'Result': sum,
            'Status Code': 200
        }

        return jsonify(retSum)


# Subtraction
class Subtract(Resource):
    def post(self):  # if am here , then Resource Subtract was requested using method POST
        # step 1 : get the posted data
        inputData = request.get_json()

        # validate the input data
        status_code = validateInputData(inputData, "subtract")

        if (status_code != 200):
            retJson = {
                "Error Description": "One of the parameters is missing.",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # if the parameters are given
        x = inputData["x"]
        y = inputData["y"]

        # step 2 : converting into integer values
        x = int(x)
        y = int(y)

        # step 3 :addition logic
        subtract = x - y

        #  step 4 :convert into json format
        retSubtract = {
            'Result': subtract,
            'Status Code': 200
        }

        return jsonify(retSubtract)


# Multiplication
class Multiply(Resource):
    def post(self):  # if am here , then Resource Subtract was requested using method POST
        # step 1 : get the posted data
        inputData = request.get_json()

        # validate the input data
        status_code = validateInputData(inputData, "multiply")

        if (status_code != 200):
            retJson = {
                "Error Description": "One of the parameters is missing.",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # if the parameters are given
        x = inputData["x"]
        y = inputData["y"]

        # step 2 : converting into integer values
        x = int(x)
        y = int(y)

        # step 3 :addition logic
        multiply = x * y

        #  step 4 :convert into json format
        retMultiply = {
            'Result': multiply,
            'Status Code': 200
        }

        return jsonify(retMultiply)


# Divide
class Divide(Resource):
    def post(self):  # if am here , then Resource Subtract was requested using method POST
        # step 1 : get the posted data
        inputData = request.get_json()

        # validate the input data
        status_code = validateInputData(inputData, "divide")


        if (status_code == 301):
            retJson = {
                "Error Description": "One of the parameters is missing.",
                "Status Code": status_code
            }
            return jsonify(retJson)
        if (status_code == 302):
            retJson = {
                "Error Description": "Cannot divide the no. by zero !",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # if the parameters are given
        x = inputData["x"]
        y = inputData["y"]

        # step 2 : converting into integer values
        x = int(x)
        y = int(y)

        # step 3 :addition logic
        divide = x / y

        #  step 4 :convert into json format
        retDivide = {
            'Result': divide,
            'Status Code': 200
        }

        return jsonify(retDivide)


# invoking the path from the URL
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


# main function
if __name__ == "__main__":
    app.run(debug=True)
