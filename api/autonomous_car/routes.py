from http import HTTPStatus

from flask import abort
from flask import jsonify
from flask import render_template

from api.autonomous_car import controllers
from app import app


@app.route('/autonomous-car/')
def automated_car_instructions():
    return render_template('autonomous-car.html')


@app.route('/autonomous-car/routes/')
def random_automated_car_route():
    return jsonify({
        'car_route': controllers.get_reliable_car_route()
    })


@app.route('/autonomous-car/routes/<string:status>/')
def automated_car_route(status):
    if not controllers.is_valid_status(status):
        abort(HTTPStatus.NOT_FOUND)
    return jsonify({
        'car_route': controllers.get_unreliable_car_route(status)
    })
