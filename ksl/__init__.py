from flask import Flask

from flask_sqlalchemy import SQLAlchemy

import ksl
from .utils.blueprint_loader import BlueprintLoader


app = Flask(__name__)

app.config.from_object('config')
app.secret_key = 'firman'
db = SQLAlchemy(app)

loader = BlueprintLoader(ksl)

blueprint_modules = [
    'ksl.anggota.blueprints',
    'ksl.articles.blueprints'
]

for module_name in blueprint_modules:
    mod = loader.load_blueprint_module(module_name)
    bps = loader.discover_blueprint_attributes(mod)
    for bp in bps:
        app.register_blueprint(bp)
