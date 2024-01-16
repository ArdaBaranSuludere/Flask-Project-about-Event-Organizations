from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin

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

class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),nullable=False)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)  # Yayın yılı
    director = db.Column(db.String(100), nullable=False)  # Yönetmen
    actors = db.Column(db.String(250))  # Oyuncular (virgülle ayrılmış liste olarak)
    poster_url = db.Column(db.String(250))  # Film posteri için URL
    price = db.Column(db.Float, nullable=False)  # Fiyat
    stock = db.Column(db.Integer, nullable=False)  # Stok

    def __repr__(self):
        return f'<Movie {self.title}>'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('CartItem', backref='cart', lazy=True)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)  # Kategori ilişkisi
    category = db.relationship('Category', backref=db.backref('products', lazy=True))
    brand = db.Column(db.String(100), nullable=True)  # Marka
    image_url = db.Column(db.String(255), nullable=True)  # Ürün resmi URL'si
    color = db.Column(db.String(50))  # Ürün rengi
    size = db.Column(db.String(50))  # Ürün boyutu
    weight = db.Column(db.Float)  # Ürün ağırlığı
    is_active = db.Column(db.Boolean, default=True)  # Ürünün aktif/pasif durumu

    def __repr__(self):
        return f'<Product {self.name}>'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'
    
# user_courses = db.Table('user_tickets',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('course_id', db.Integer, db.ForeignKey('course.id')))

# forms.py