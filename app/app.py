from flask import Flask
from blueprints.login import login_blueprint
from db import db

# Melhor colocar o nome do pacote (app) do que o __name__
def create_app(mode=None):
  app = Flask('app')
  if mode:
    app.config.from_object('config.%sConfig' %mode)

  app.register_blueprint(login_blueprint)

  db.init_app(app)

  return app
