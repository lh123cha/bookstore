from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import user
from be.model import store
from be.model import order

bp_order = Blueprint("order", __name__, url_prefix="/order")


@bp_order.route("/getOrder", methods=["POST"])
def getOrder():
    username = request.json.get("username", "")
    ok, orderlist = order.getOrder(username=username)

    if ok:
        return jsonify({"message": "ok", "orderlist": orderlist}), 200
    else:
        return jsonify({"message": "Orderid Is NULL"}), 503