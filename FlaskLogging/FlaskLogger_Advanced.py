from flask import Flask,request,make_response
import logging
import logging.config

app = Flask(__name__)

logging.config.fileConfig(fname='loggingConfig.conf')
logger = logging.getLogger(__name__)

@app.route('/')
def main():
    try:
        result = 5/0
        logger.info('Info level log')
        return {'result':result}
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero.')

@app.route('/login',methods=['POST'])
def login():
    auth = request.authorization

    if auth.username == 'abc' and auth.password == '123':
        logger.info('%s logged in successfully',auth.username)
        return make_response('Welcome',200)
    elif auth.username == '' or auth.password == '':
        logger.warning('One of the field is left blank')
        return make_response('Field could not be left blank',400)
    else:
        logger.error('Failed to Login')
        return make_response('Failed to Login.',401)


if __name__ == "__main__":
    app.run()