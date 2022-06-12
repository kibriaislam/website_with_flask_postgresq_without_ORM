from flask import Blueprint, render_template,request
from db_connection import db_conn


registration_bp = Blueprint('registration_bp',__name__,
        template_folder = 'templates',
        static_folder = 'static')


@registration_bp.route('/signup',methods=["POST"])
def registration():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if username and password and email:
               





