'''
Module to handle Transaction related apis
'''

# imports 
from flask import Blueprint, jsonify, request, session
from .utils import sponcer_login_required
from ..models import Sponcers
from .. import db

# registering blueprint
tranx = Blueprint("tranx", __name__)

# add money to sponcer
@tranx.route('/check')
def check():
    return jsonify({
        'status' : 'success'
    }), 200


# add money to sponcers
@tranx.route('/credit', methods=['POST'])
@sponcer_login_required
def credit():
    try:
        data = {
            'id' : request.args.get('id'),
            'amount' : request.args.get('amount'),
            'upiId' : request.args.get('upiId')
        }
        # check wheather it is above 100 or not
        assert float(data['amount']) > 100

        user = Sponcers.query.filter_by(id=int(data['id'])).first()
        user.balance = user.balance + float(data['amount'])

        db.session.commit()

        return jsonify({
            'status' : 'success',
            'updt_amt' : user.balance
        }), 200

    except AssertionError as e:
        return jsonify({
            'status' : 'failed',
            'error' : 'Amount is not sufficient.'
        }), 400
    
    except Exception as e:
        return jsonify({
            'status' : 'failed',
            'error' : 'some error occured.',
            'error_desc' : str(e)
        }), 400
