from flask import current_app
from app import db

class Admin(db.Model):
  """An admin user capable of view restrict area.
  :param str username: text
  :param str password: text
  """
  __tablename__ = 'admin'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.Text(128), nullable=False)

  def __repr__(self):
    return 'Admin %r' % self.username
