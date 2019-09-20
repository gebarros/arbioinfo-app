import os
import sys

def load_env_vars(filename):
  if os.path.exists(filename):
      for line in open(filename):
          var = line.strip().split('=')
          if len(var) == 2:
              os.environ[var[0]] = var[1]
          elif len(var) > 2:
              os.environ[var[0]] = "=".join(var[1:])
  else:
      print("You need to have {} file with required env vars.".format(filename))
      sys.exit()

class BaseConfig(object):
  load_env_vars(".env")
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

class DevelopmentConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")

class ProductionConfig(BaseConfig):
  DEBUG = True




