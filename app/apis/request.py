'''
Module to handle APIs regarding diffrent requests
'''

# imports
from flask import Blueprint, jsonify, request, session
from .utils import sponcer_login_required
from ..models import Sponcers, AddRequests, SponcerRequests, Influencers
from .. import db
import logging

# registering blueprint
request_api = Blueprint("request", __name__)


# Delete Ad request api
@request_api.route("/cancelAdRequest/<int:id>", methods=["POST"])
@sponcer_login_required
def cancelAdRequest(id):
    try:
        ad = AddRequests.query.get(int(id))

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
    


# update ad request
@request_api.route("/updateAdRequest/<int:id>", methods=["POST"])
@sponcer_login_required
def updateAdRequest(id):
    try:
        data = request.json
        if not data:
            logging.warning("Invalid request")
            return jsonify({"status": "failed", "error": "Invalid request"}), 400

        ad = AddRequests.query.get(int(id))

        if not ad:
            logging.warning("Ad not found")
            return jsonify({"status": "failed", "error": "Ad request_api not found"}), 404

        if ('id' not in session) or (ad.sponcer.id != session["id"]):
            logging.warning("Unauthorized Access")
            return jsonify({"status": "failed", "error": "Unauthorized Access"}), 401
        
        # updating data in data base
        ad.requirements = data["requirements"]
        ad.message = data["message"]
        ad.payment = data["payment"]

        db.session.commit()

        return jsonify({"status": "success", "message": "Ad request updated successfully"}), 200

    except Exception as e:
        logging.error(e)
        return jsonify({"status": "failed", "error": str(e)}), 400
    


# accept proposal
@request_api.route("/acceptProposal/<int:id>", methods=["POST"])
@sponcer_login_required
def acceptProposal(id):
    try:
        proposal = SponcerRequests.query.get(int(id))

        if not proposal:
            logging.warning("Proposal not found")
            return jsonify({"status": "failed", "error": "Proposal not found"}), 404
        
        if ('id' not in session) or (proposal.sponcer.id != session["id"]):
            logging.warning("Unauthorized Access")
            return jsonify({"status": "failed", "error": "Unauthorized Access"}), 401
        
        # check does sponcer have money to pay
        if proposal.sponcer.balance < proposal.payment:
            logging.warning("Insufficient money")
            return jsonify({"status": "failed", "error": "Insufficient Balance"}), 400
        
        # updating data in data base
        proposal.status = 'accepted'
        
        # deduct balance from sponcer
        sp = Sponcers.query.get(proposal.spo_id)
        sp.balance = sp.balance - proposal.payment

        # add balance to sponcer
        inf = Influencers.query.get(proposal.inf_id)
        inf.balance = inf.balance + proposal.payment

        # saving changes
        db.session.commit()

        return jsonify({"status": "success", "message": "Proposal accepted successfully"}), 200
    
    except Exception as e:
        logging.error(e)
        return jsonify({"status": "failed", "error": str(e)}), 400


# reject proposal
@request_api.route("/rejectProposal/<int:id>", methods=["POST"])
@sponcer_login_required
def rejectProposal(id):
    try:
        proposal = SponcerRequests.query.get(int(id))
        
        if not proposal:
            logging.warning("Proposal not found")
            return jsonify({"status": "failed", "error": "Proposal not found"}), 404
        
        if ('id' not in session) or (proposal.sponcer.id != session["id"]):
            logging.warning("Unauthorized Access")
            return jsonify({"status": "failed", "error": "Unauthorized Access"}), 401
        
        # updating data in data base
        proposal.status = 'rejected'    

        # saving changes
        db.session.commit()

        return jsonify({"status": "success", "message": "Proposal rejected successfully"}), 200

    except Exception as e:
        logging.error(e)
        return jsonify({"status": "failed", "error": str(e)}), 400
    