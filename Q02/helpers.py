from flask import jsonify
from sqlalchemy import desc

class DataTables():
    def __init__(self, model, request_params):
        self.model = model
        self.request_params = request_params

    def get_paginated_results(self, page, per_page, order_by, order_type):
        result = self.model.query.order_by(order_by)  #
        if order_type == "desc":
            result = self.model.query.order_by(desc(order_by))
        paginated = result.paginate(page=page, per_page=per_page)
        return paginated

    def _make_response(self, draw, recordsTotal, recordsFiltered, data, *error):
        final_response = {}
        try:
            draw = int(draw)
            final_response["draw"] = draw
        except ValueError:
            error = {"draw": "Error while casting draw to integer."}
            final_response["error"] = error
            return final_response
        final_response["recordsTotal"] = recordsTotal
        final_response["recordsFiltered"] = recordsFiltered
        final_response["data"] = data
        return jsonify(final_response)

    def get_response(self):
        draw = self.request_params.get("draw")
        record_number = self.request_params.get("start")
        per_page = self.request_params.get("length")
        page_number = int(record_number / per_page) + 1
        order_column_identifier = self.request_params.get("order")[0].get("column")
        order_type = self.request_params.get("order")[0].get("dir")
        order_by_column = self.request_params.get("columns")[order_column_identifier].get("data")
        result = self.get_paginated_results(page=page_number, per_page=per_page, order_type=order_type,
                                            order_by=order_by_column)
        data = [user_data.serialize() for user_data in result.items]
        recordsTotal = recordsFiltered = result.total
        response = self._make_response(draw=draw, recordsTotal=recordsTotal, recordsFiltered=recordsFiltered, data=data)
        return response
