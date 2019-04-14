from flask import Flask

app = Flask(__name__)

from .views import login
app.register_blueprint(login.mod)