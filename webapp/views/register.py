from flask import Blueprint, render_template

mod = Blueprint('register', __name__)

@mod.route('/register')
def login() :
	pass