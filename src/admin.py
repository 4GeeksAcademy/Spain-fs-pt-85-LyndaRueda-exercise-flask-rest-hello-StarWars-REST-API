import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from wtforms import PasswordField
from wtforms.validators import InputRequired
from models import db, User, Character, Episode, Location, Favorite

class UserAdmin(ModelView):
    form_base_class = SecureForm

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Rick and Morty Admin', template_mode='bootstrap3')

    # Modelos al panel de adminin con vistas personalizadas para c/u
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Episode, db.session))
    admin.add_view(ModelView(Location, db.session))
    admin.add_view(ModelView(Favorite, db.session))
