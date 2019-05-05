from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from consoleapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
csrf = CSRFProtect()
csrf.init_app(app)

login = LoginManager(app)
login.login_view = 'login.login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:vision@localhost/UserInfoDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .views import login
app.register_blueprint(login.mod)

from .views import register
app.register_blueprint(register.reg)

from .views import index
app.register_blueprint(index.home)

from .views import logout
app.register_blueprint(logout.mod1)

from .views import user_control_panel
app.register_blueprint(user_control_panel.adminmod1)

from .views import new_project
app.register_blueprint(new_project.new_proj)

from .views import project
app.register_blueprint(project.proj)

from .views import models



db.create_all()
db.session()