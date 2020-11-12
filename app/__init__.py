"Main application module"
from flask import Flask

from config import Config
from app.db.install import install

app = Flask(__name__)
app.config.from_object(Config)

from app.api import bp as api, routes
app.register_blueprint(api, url_prefix='/api')

@app.route('/install')
def installation():
    install()
    return "Great! Installed ;) "
