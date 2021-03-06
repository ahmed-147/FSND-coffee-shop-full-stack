import os
import sys
import json
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from flask_cors import CORS
from flasgger import Swagger
from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
Swagger(app)
setup_db(app)
CORS(app)


'''
@DONE uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''


# db_drop_and_create_all()


'''
ROUTES

@DONE implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and
    json {
        "success": True,
        "drinks": drinks
    }
    where drinks is the list of drinks
    or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['GET'])
def get_drinks():

    drinks = Drink.query.all()
    if drinks is None:
        abort(404)

    return jsonify({'success': True,
                    'drinks': [d.short() for d in drinks]
                    })


'''
@DONE implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and
    json {
        "success": True,
        "drinks": drinks
    }
    where drinks is the list of drinks
    or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):

    drinks = Drink.query.all()
    if drinks is None:
        abort(404)

    return jsonify({"success": True,
                    "drinks": [d.long() for d in drinks]
                    })


'''
@DONE implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and
    json {
        "success": True,
        "drinks": drink
    }
    where drink an array containing only the newly created drink
    or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_new_drinks(payload):

    req = request.get_json()
    req_title = req.get('title', ' ')
    req_recipe = req.get('recipe', None)
    try:

        if type(req_recipe) == str:
            recipe = req_recipe
        else:
            recipe = json.dumps(req_recipe)

        drink = Drink(title=req_title, recipe=json.dumps(req_recipe))
        drink.insert()

        return jsonify({"success": True,
                        "drinks": [drink.long()]
                        }), 200
    except Exception as ea:
        print(ea, sys.exc_info())
        abort(400)


'''
@DONE implement endpoint
    PATCH /drinks/<id>
            where <id> is the existing model id
            it should respond with a 404 error if <id> is not found
            it should update the corresponding row for <id>
            it should require the 'patch:drinks' permission
            it should contain the drink.long() data representation
        returns status code 200 and
        json {
        "success": True,
        "drinks":drink
        }
        where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drinks(payload, id):

    req = request.get_json()
    drink = Drink.query.filter_by(id=id).one_or_none()

    if drink is None:
        abort(404)
    try:
        req_title = req.get('title', '')
        req_recipe = req.get('recipe', None)

        if req_title:
            drink.title = req_title

        if req_recipe:
            if type(req_recipe) == str:
                drink.recipe = req_recipe
            else:
                drink.recipe = json.dumps(req_recipe)

        drink.update()

    except BaseException:
        abort(400)

    return jsonify({"success": True,
                    "drinks": [drink.long()]
                    }), 200


'''
@DONE implement endpoint
    DELETE /drinks/<id>
    where <id> is the existing model id
    it should respond with a 404 error if <id> is not found
    it should delete the corresponding row for <id>
    it should require the 'delete:drinks' permission
    returns status code 200 and
    json {
        "success": True,
        "delete": id
    }
    where id is the id of the deleted record
    or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(payload, id):

    drink = Drink.query.filter_by(id=id).one_or_none()

    if drink is None:
        abort(404)
    else:
        drink.delete()

    drinks = Drink.query.all()

    if not drinks:
        abort(404)

    return jsonify({"success": True,
                    "drinks": [d.long() for d in drinks]
                    }), 200


'''
Error Handling
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False,
                    "error": 422,
                    "message": "unprocessable"
                    }), 422


'''
@DONE implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''
'''
@DONE implement error handler for 404
    error handler should conform to general task above
'''


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404


'''
@DONE implement error handler for AuthError
    error handler should conform to general task above
'''


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": 'Unathorized'
    }), 401


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": 'Internal Server Error'
    }), 500


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": 'Bad Request'
    }), 400


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": 'Method Not Allowed'
    }), 405
