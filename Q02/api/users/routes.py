import json
from datetime import datetime

from flask import request, Blueprint, jsonify, render_template

from Q02 import db
from Q02.helpers import DataTables
from Q02.models import UsersModel

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/users/', methods=['POST'])
def userLst():
    request_params = json.loads(request.values.get("args"))
    response = DataTables(model=UsersModel, request_params=request_params).get_response()
    return response


# @api.route('/users')
# def userLst():
#     pass


@api.route('/users/add', methods=['GET', 'POST'])
def userAdd():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        start_date = user_data.get("start_date")
        user_data["start_date"] = datetime.strptime(start_date, '%Y-%m-%d')
        user_instance = UsersModel(**user_data)
        db.session.add(user_instance)
        db.session.commit()
        response = {"user_id": user_instance.id}
        return jsonify(response)
    return render_template("add_edit_users.html", add=True)


# @api.route('/users/<int:uid>')
# def userRead(uid):
#     pass


@api.route('/users/<int:uid>', methods=['PATCH', 'GET'])
def userPatch(uid):
    user = UsersModel.query.filter_by(id=uid).first()
    if request.method == 'GET':
        if user is None:
            response_kwargs = {"error": "User ID does not exist", "edit": True}
            return render_template("add_edit_users.html", **response_kwargs)
        response_kwargs = user.serialize()
        response_kwargs["edit"] = True
        return render_template("add_edit_users.html", **response_kwargs)
    else:
        updated_data = request.form.to_dict()
        start_date = updated_data.get("start_date")
        updated_data["start_date"] = datetime.strptime(start_date, '%Y-%m-%d')
        for key, val in updated_data.items():
            setattr(user, key, val)
        db.session.commit()
        return jsonify(user.serialize())





@api.route('/users/<int:uid>', methods=['DELETE'])
def userDelete(uid):
    user = UsersModel.query.filter_by(id=uid).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        response = {"user_id": user.id}
    else:
        response = {"error": "User ID does not exist"}

    response = jsonify(response)

    return response
