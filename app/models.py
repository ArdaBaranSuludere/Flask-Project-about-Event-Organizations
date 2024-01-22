
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin

if not 'Etkinlikler' in locals():
    class Etkinlikler(db.Model):
        etkinlik_id = db.Column(db.Integer, primary_key=True)
        etkinlik_ad = db.Column(db.String(100),nullable=False)
        etkinlik_turu = db.Column(db.String(100),nullable=False)
        etkinlik_yeri = db.Column(db.String(100),nullable=False)
        etkinlik_tarih = db.Column(db.Date, nullable=False)
        etkinlik_baslangic_saati = db.Column(db.Integer, nullable=False)
        etkinlik_bitis_saati = db.Column(db.Integer, nullable=False)
        kapasite = db.Column(db.Integer, nullable=False)
        bilet_id = db.Column(db.Integer, nullable=False)
        users = db.relationship('User', secondary='user_etkinliks', back_populates='etkinliks')


if not 'User' in locals():
    class User(UserMixin, db.Model):
        table_args = {'extend_existing': True}
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), index=True, unique=True)
        email = db.Column(db.String(120), index=True, unique=True)
        password_hash = db.Column(db.String(256))
        is_admin = db.Column(db.Boolean, default=False)

        etkinliks = db.relationship('Etkinlikler', secondary='user_etkinliks', back_populates='users')

        def __repr__(self):
            return '<User {}>'.format(self.username)

        def set_password(self, password):
            self.password_hash = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password_hash, password)

user_etkinliks = db.Table('user_etkinliks',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('etkinlik_id', db.Integer, db.ForeignKey('etkinlikler.etkinlik_id'))
)

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

        def __repr__(self):
            return f'<RezervBasvurulari {self.name}>'

if not 'Newsletter' in locals():
    class Newsletter(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120),nullable=False)

        def __repr__(self):
            return f'<Newsletter {self.email}>'

# forms.py
    