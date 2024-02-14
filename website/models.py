from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db


class CustomSessionModel(db.Model):
    __tablename__ = "sessions"

    session_id = db.Column(db.String(255), primary_key=True)
    data = db.Column(db.Text)
    expiry = db.Column(db.DateTime)
    modified = db.Column(db.DateTime, default=datetime.utcnow)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200))
    category = db.Column(db.String(100))

    sizes = db.relationship("Size", backref="product", cascade="all, delete-orphan")

    favorites = db.relationship(
        "User", secondary="favorites", backref=db.backref("favorites", lazy="dynamic")
    )


class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    size_id = db.Column(db.Integer, db.ForeignKey("size.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)


class Favorites(db.Model):
    __tablename__ = "favorites"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship(
        "User", backref=db.backref("favorites_assoc", cascade="all, delete-orphan")
    )

    product = db.relationship(
        "Product", backref=db.backref("users_assoc", cascade="all, delete-orphan")
    )


class UserFavoritesCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True)
    favorites_count = db.Column(db.Integer, default=0)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    favorite_products = db.relationship(
        "Product", secondary="favorites", backref=db.backref("users", lazy="dynamic")
    )

    def add_to_favorites(self, product):
        if product not in self.favorite_products:
            self.favorite_products.append(product)

    def has_favorited(self, product):
        return product in self.favorites

    def get_favorites_count(self):
        return Favorites.query.filter_by(user_id=self.id).count()

    def get_favorites(self):
        return self.favorites.all()
