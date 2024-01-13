
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from os import path
from flask_babel import Babel
from flask_admin.contrib.sqla import ModelView


# Uygulama ve Veritabanı Yapılandırması
app = Flask(__name__)
babel = Babel(app)
basedir = path.abspath(path.dirname(__file__))
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'site.db')


# Uygulama Eklentileri
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.init_app(app)
from app.my_admin.routes import MyAdminIndexView
admin = Admin(app, name='Admin', index_view=MyAdminIndexView(), template_mode='bootstrap3')

# Model ve View İçe Aktarmaları
from app.models import Product, Category, User, Etkinlikler, RezervBasvurulari, Newsletter
from app.my_admin import ProductModelView, CategoryModelView, UserModelView
from app.auth import auth as auth_blueprint

# Admin Paneli
admin.add_view(UserModelView(User, db.session))
admin.add_view(ProductModelView(Product, db.session))
admin.add_view(CategoryModelView(Category, db.session))


app.register_blueprint(auth_blueprint, url_prefix='/auth')

from app import views, models
from app.models import User

from app import app, db
from app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if not 'Etkinlikler' in locals():
    class Etkinlikler(db.Model):
        etkinlik_id = db.Column(db.Integer,primary_key=True)
        etkinlik_ad = db.Column(db.String(100),nullable=False)
        etkinlik_turu = db.Column(db.String(100),nullable=False)
        etkinlik_yeri = db.Column(db.String(100),nullable=False)
        etkinlik_tarih = db.Column(db.Date, nullable=False)
        etkinlik_baslangic_saati = db.Column(db.Integer, nullable=False)
        etkinlik_bitis_saati = db.Column(db.Integer, nullable=False)
        kapasite = db.Column(db.Integer, nullable=False)
        bilet_id = db.Column(db.Integer, nullable=False)

admin.add_view(ModelView(Etkinlikler,db.session))


if not 'RezervBasvurulari' in locals():
    class RezervBasvurulari(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120),nullable=False)
        name = db.Column(db.String(100),nullable=False)
        phone_number = db.Column(db.String(15),nullable=False)
        company = db.Column(db.String(100),nullable=False)
        venue_requested = db.Column(db.Integer, nullable=False)
        type_of_event = db.Column(db.String(100),nullable=False)
        date_requested_primary = db.Column(db.Date, nullable=False)
        date_requested_secondary = db.Column(db.Date, nullable=False)
        about_event = db.Column(db.String(100),nullable=False)

admin.add_view(ModelView(RezervBasvurulari,db.session))

if not 'Newsletter' in locals():
    class Newsletter(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120),nullable=False)


admin.add_view(ModelView(Newsletter,db.session))
