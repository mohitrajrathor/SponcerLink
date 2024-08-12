'''
Module to handle APIs regarding diffrent requests
'''

# imports
from flask import Blueprint, jsonify, request, session
from .utils import sponcer_login_required
from ..models import Sponcers
from .. import db
from ..models import AddRequests
import logging

# registering blueprint
request = Blueprint("request", __name__)


# Delete Ad request api
@request.route("/cancelAdRequest/<int:id>", methods=["POST"])
# @sponcer_login_required
def cancelAdRequest(id):
    try:
        ad = AddRequests.query.get(int(id))

        print(ad)

        if not ad:
            logging.warning("Ad not found")
            return jsonify({"status": "failed", "error": "Ad request not found"}), 404

        if ('id' not in session) or (ad.sponcer.id != session["id"]):
            logging.warning("Unauthorized Access")
            return jsonify({"status": "failed", "error": "Unauthorized Access"}), 401
        
        ad.status = 'cancelled'

        db.session.commit()
        return jsonify({"status": "success", "message": "Ad request cancelled successfully"}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({"status": "failed", "error": str(e)}), 400