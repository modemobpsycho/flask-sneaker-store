from flask import Blueprint, render_template
from flask_login import login_required, current_user, user_accessed
from .models import Product, Size
from . import db
views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template('base.html', user=current_user)


@views.route('/cart')
@login_required
def cart():
    return render_template('cart.html', user=current_user)


@views.route('/order')
@login_required
def order():
    return render_template('order.html', user=current_user)


@views.route('/product')
@login_required
def product_page():
    products = Product.query.all()
    sizes = Size.query.all()
    return render_template('product.html', products=products, sizes=sizes, user=current_user)


@views.route('/checkout')
@login_required
def checkout():
    return render_template('checkout.html', user=current_user)

@views.route('/category')
def category():
    return render_template('category.html', user=current_user)
