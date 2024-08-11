from flask import Flask
from flask import Blueprint, session, url_for, redirect, render_template


influencer = Blueprint('influencer', __name__, url_prefix='/influencer')