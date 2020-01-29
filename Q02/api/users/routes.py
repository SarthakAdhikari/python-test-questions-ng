import json

from flask import request, Blueprint

from Q02.helpers import DataTables
from Q02.models import UsersModel

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/users/', methods=['POST'])
def userLst():
    request_params = json.loads(request.values.get("args"))
    response = DataTables(model=UsersModel, request_params=request_params).get_response()
    return response
