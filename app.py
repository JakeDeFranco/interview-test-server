from flask import Flask, render_template, jsonify
from flask_cors import CORS

from api.error_handlers import format_error

app = Flask(__name__)
CORS(app)


@app.route('/')
def instructions():
    return render_template('instructions.html')


@app.errorhandler(404)
def not_found_handler(e):
    return jsonify({
        'errors': format_error(
            message='That url was not found',
            code='NOT_FOUND'
        )
    }), 404


@app.errorhandler(Exception)
def exception_handler(e):
    return jsonify({
        'errors': format_error(
            message=str(e),
            code='INTERNAL_SERVER_ERROR'
        )
    }), 500


from api.tax_calculator.routes import *
from api.autonomous_car.routes import *
