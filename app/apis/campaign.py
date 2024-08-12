'''
Module to handle Campaign related apis
'''

# imports
import logging
from flask import Blueprint, jsonify, request, session
from .utils import sponcer_login_required
from ..models import Sponcers, Campaigns
from .. import db
import datetime as dt


# registering blueprint
campaign_api = Blueprint("campaign_api", __name__)


# create campaign_api api
@campaign_api.route("/createCampaign", methods=["POST"])
@sponcer_login_required
def createCampaign():
    try:
        data = request.json
        if not data:
            logging.warning("Invalid request")
            return jsonify({"status": "failed", "error": "Invalid request"}), 400

        if ('id' not in session):
            logging.warning("Unauthorized Access")
            return jsonify({"status": "failed", "error": "Unauthorized Access"}), 401

        try:
            if float(data['budget']) < 0:
                logging.warning("Invalid budget")
                return jsonify({"status": "failed", "error": "Invalid budget"}), 400
        except:
            logging.warning("Invalid budget")
            return jsonify({"status": "failed", "error": "Budget must be number"}), 400

        campaign_api = Campaigns(
            spo_id=session["id"],
            title=data["title"],
            description=data["description"],
            requirements=data["requirements"],
            budget=float(data["budget"]),
            start_date=data["start_date"],
            end_date=data["end_date"],
            post_time=str(dt.datetime.now().isoformat())
        )

        # updating data in data base
        db.session.add(campaign_api)
        db.session.commit()
        return jsonify({"status": "success", "message": "Campaign created successfully"}), 200

    except Exception as e:
        logging.error(e)
        return jsonify({"status": "failed", "error": str(e)}), 400
    


# update campaign_api api
@campaign_api.route("/updateCampaign/<int:id>", methods=["PUT"])
@sponcer_login_required
def updateCampaign(id):
    try:
        data = request.json
        if not data:
            logging.warning("Invalid request")
            return jsonify({"status": "failed", "error": "Invalid request"}), 400
        
        if ('id' not in session) or (Campaigns.query.get(id).spo_id != session["id"]):
            logging.warning("Unauthorized Access")
            return jsonify({"status": "failed", "error": "Unauthorized Access"}), 401

        campaign_api = Campaigns.query.get(id)

        if not campaign_api:
            logging.warning("Campaign not found")
            return jsonify({"status": "failed", "error": "Campaign not found"}), 404
        
        # updating data in data base
        campaign_api.title = data["title"]
        campaign_api.description = data["description"]
        campaign_api.requirements = data["requirements"]
        campaign_api.budget = float(data["budget"])
        campaign_api.start_date = data["start_date"]
        campaign_api.end_date = data["end_date"]

        db.session.commit()
        return jsonify({"status": "success", "message": "Campaign updated successfully"}), 200

    except Exception as e:
        logging.error(e)
        return jsonify({"status": "failed", "error": str(e)}), 400
    

# delete campaign_api api
@campaign_api.route("/deleteCampaign/<int:id>", methods=["DELETE"])
@sponcer_login_required
def deleteCampaign(id):
    try:
        if ('id' not in session) or (Campaigns.query.get(id).spo_id != session["id"]):
            logging.warning("Unauthorized Access")
            return jsonify({"status": "failed", "error": "Unauthorized Access"}), 401   

        campaign_api = Campaigns.query.get(id)

        if not campaign_api:
            logging.warning("Campaign not found")
            return jsonify({"status": "failed", "error": "Campaign not found"}), 404

        db.session.delete(campaign_api)
        db.session.commit()
        return jsonify({"status": "success", "message": "Campaign deleted successfully"}), 200

    except Exception as e:
        logging.error(e)
        return jsonify({"status": "failed", "error": str(e)}), 400
    