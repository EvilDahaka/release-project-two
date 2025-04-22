from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for
from models import get_db_connection, get_products
from .user import auth

products_bp = Blueprint('products', __name__)

get_db_connection()

@products_bp.before_request
def check_auth():
    if not auth():  # Викликається перед кожним запитом до цього блоку
        return redirect(url_for('user.login'))

# Сторінка продуктів із фільтром за тегом
@products_bp.route('/products')
def products():

    tag = request.args.get('tag')
    products = get_products(tag=tag)
    return render_template('products.html', products=products)