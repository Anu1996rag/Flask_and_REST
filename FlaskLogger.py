from flask import Flask,request,make_response
import logging

app = Flask(__name__)

logging.basicConfig(filename='appLogs.log',format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def main():
    try:
        result = 5/0
        app.logger.info('Info level log')
        return {'result':result}
    except ZeroDivisionError:
        app.logger.exception('Tried to divide by zero.')

@app.route('/login',methods=['POST'])
def login():
    auth = request.authorization

    if auth.username == 'abc' and auth.password == '123':
        app.logger.info('%s logged in successfully',auth.username)
        return make_response('Welcome',200)
    elif auth.username == '' or auth.password == '':
        app.logger.warning('One of the field is left blank')
        return make_response('Field could not be left blank',400)
    else:
        app.logger.error('Failed to Login')
        return make_response('Failed to Login.',401)


if __name__ == "__main__":
    app.run()