from flask import Blueprint, render_template

mod = Blueprint('login', __name__)

@mod.route('/login')
def login() :
	pass
