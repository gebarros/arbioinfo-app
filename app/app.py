from flask import Flask

from blueprints.login import login_blueprint

# Melhor colocar o nome do pacote (app) do que o __name__
def create_app(config_filename=None):
  app = Flask('app')
  if config_filename:
    app.config.from_pyfile(config_filename)

  app.register_blueprint(login_blueprint)

  return app
