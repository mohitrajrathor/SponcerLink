'''
module to create common reusable functionalities.
'''

#  imports 
from functools import wraps
from flask import session, jsonify



# 
def sponcer_login_required(f):
    '''
    decorator to handle sponcer login reqiurement.
    '''
    @wraps(f)
    def decorator_func(*args, **kwargs):
        if 'id' not in session:
            return jsonify({
                'error' : 'not authorize to perform this action.'
            }), 401
        return f(*args, **kwargs)
    return decorator_func