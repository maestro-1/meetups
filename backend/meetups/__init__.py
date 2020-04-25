from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import DevelopConfig

app = Flask(__name__)

app.config.from_object(DevelopConfig)
CORS(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from .events.routes import events
from .users.routes import users
from .main.routes import main
from .guests.routes import guests
from .errors.handlers import errors

app.register_blueprint(events)
app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(guests)
app.register_blueprint(errors)
