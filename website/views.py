from flask import Blueprint, flash, redirect, render_template, request, url_for, session
from flask_login import login_required, current_user
from sqlalchemy import func
from .models import Favorites, Product, Size, UserFavoritesCount
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("base.html", user=current_user)


@views.route("/cart")
@login_required
def cart():
    return render_template("cart.html", user=current_user)


@views.route("/favorites")
@login_required
def favorites():
    favorites_count = current_user.get_favorites_count()
    favorites = Favorites.query.filter_by(user_id=current_user.id).all()
    user_favorites = []

    for favorite in favorites:
        product = Product.query.get(favorite.product_id)
        user_favorites.append(product)

    return render_template(
        "favorites.html",
        favorites_count=favorites_count,
        user_favorites=user_favorites,
        user=current_user,
    )


@views.route("/order")
@login_required
def order():
    return render_template("order.html", user=current_user)


@views.route("/product")
@login_required
def product_page():
    products = Product.query.all()
    sizes = Size.query.all()
    return render_template(
        "product.html", products=products, sizes=sizes, user=current_user
    )


@views.route("/checkout")
@login_required
def checkout():
    return render_template("checkout.html", user=current_user)


@views.route("/category")
def category():
    return render_template("category.html", user=current_user)


@views.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        search_query = request.args.get("search_query")
        if search_query is not None:
            products = Product.query.filter(
                func.lower(Product.name).like(f"%{search_query.lower()}%")
            ).all()
        else:
            products = []
        return render_template(
            "search.html", products=products, query=search_query, user=current_user
        )
    else:
        return render_template("search.html", user=current_user)


@views.route("/add-to-cart", methods=["GET"])
@login_required
def add_to_cart():
    product_id = request.args.get("product_id")

    return redirect(url_for("views.cart"))


@views.route("/add-to-favorites", methods=["POST"])
@login_required
def add_to_favorites():
    product_id = request.form.get("product_id")
    product_id = int(product_id)

    product = Product.query.get(product_id)

    if product:
        if not current_user.has_favorited(product):
            current_user.add_to_favorites(product)
            db.session.commit()

            user_favorites_count = UserFavoritesCount.query.filter_by(
                user_id=current_user.id
            ).first()
            if user_favorites_count:
                user_favorites_count.favorites_count += 1
            else:
                user_favorites_count = UserFavoritesCount(
                    user_id=current_user.id, favorites_count=1
                )
                db.session.add(user_favorites_count)

            db.session.commit()

            session["favorites_count"] = user_favorites_count.favorites_count

        else:
            flash("Product already exist!", "info")
    else:
        flash("Product is undefined!", "error")

    return redirect(request.referrer or url_for("views.favorites"))
