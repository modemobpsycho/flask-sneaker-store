from flask import Blueprint, flash, redirect, render_template, request, url_for
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


@views.route('/add-to-cart', methods=['GET'])
@login_required
def add_to_cart():
    product_id = request.args.get('product_id')

    return redirect(url_for('views.cart'))


@views.route('/add-to-favorites', methods=['GET', 'POST'])
@login_required
def add_to_favorites():
    if request.method == "POST":
        product_id = request.form.get('product_id')

        if product_id:
            try:
                product_id = int(product_id)
            except ValueError:
                flash('Неправильный идентификатор товара!', 'error')
                return redirect(request.referrer or url_for('views.home'))

            product = Product.query.get(product_id)

            if product:
                current_user.add_to_favorites(product)
                db.session.commit()
                flash('Товар успешно добавлен в избранные!', 'success')
            else:
                flash('Товар не найден!', 'error')
        else:
            flash('Неправильный идентификатор товара!', 'error')

    return redirect(request.referrer or url_for('views.cart'))