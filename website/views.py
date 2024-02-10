from flask import Blueprint, render_template
from flask_login import login_required, current_user, user_accessed

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template('home.html', user=current_user)


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
def product():
    return render_template('product.html', user=current_user)


@views.route('/checkout')
@login_required
def checkout():
    return render_template('checkout.html', user=current_user)

@views.route('/category')
def category():
    return render_template('category.html', user=current_user)
