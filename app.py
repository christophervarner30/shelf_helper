from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, abort, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, login_required, current_user
from extensions import db
from flask_babel import Babel, _, get_locale
from auth import auth_bp
from werkzeug.security import check_password_hash
from flask_wtf import CSRFProtect
from wtforms import Form, StringField, PasswordField, FloatField, IntegerField, BooleanField, validators

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shelf_helper.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-placeholder-key-d8f3f9s7fs8f7s89')
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] = ['en', 'es']
db.init_app(app)
csrf = CSRFProtect(app)
babel = Babel(app)

# Database Models
from models import User

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    shelf_location = db.Column(db.String(50))
    stock = db.Column(db.Integer, default=0)
    category = db.Column(db.String(50))
    high_shelf = db.Column(db.Boolean, default=False)  # True if on highest/out-of-reach shelf
    image_url = db.Column(db.String(300))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    customer_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    store = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Flask-Login setup
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprint
app.register_blueprint(auth_bp)

# WTForms for input validation
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=3, max=25), validators.DataRequired()])
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=8), validators.DataRequired()])

class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class ProductForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100), validators.DataRequired()])
    description = StringField('Description', [validators.Length(max=500)])
    price = FloatField('Price', [validators.DataRequired()])
    shelf_location = StringField('Shelf Location', [validators.Length(max=50)])
    stock = IntegerField('Stock', [validators.DataRequired()])
    category = StringField('Category', [validators.Length(max=50)])
    high_shelf = BooleanField('High Shelf')
    image_url = StringField('Image URL', [validators.Length(max=300)])

class OrderForm(Form):
    product_id = IntegerField('Product ID', [validators.DataRequired()])
    customer_name = StringField('Customer Name', [validators.Length(max=100)])
    store = StringField('Store', [validators.Length(max=50), validators.DataRequired()])

# Routes
@app.route('/')
def index():
    search = request.args.get('search', '').strip()
    category = request.args.get('category', '').strip()
    shelf_location = request.args.get('shelf_location', '').strip()
    min_price = request.args.get('min_price', '').strip()
    max_price = request.args.get('max_price', '').strip()
    stock_status = request.args.get('stock_status', '').strip()
    shelf_locations = [row[0] for row in db.session.query(Product.shelf_location).distinct().all() if row[0]]
    categories = [row[0] for row in db.session.query(Product.category).distinct().all() if row[0]]
    query = Product.query
    if search:
        query = query.filter((Product.name.ilike(f'%{search}%')) | (Product.description.ilike(f'%{search}%')))
    if category:
        query = query.filter(Product.category == category)
    if shelf_location:
        query = query.filter(Product.shelf_location == shelf_location)
    if min_price:
        try:
            query = query.filter(Product.price >= float(min_price))
        except ValueError:
            pass
    if max_price:
        try:
            query = query.filter(Product.price <= float(max_price))
        except ValueError:
            pass
    if stock_status == 'in':
        query = query.filter(Product.stock > 0)
    elif stock_status == 'out':
        query = query.filter(Product.stock <= 0)
    products = query.all()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Render only the product grid for AJAX
        return make_response(render_template('index.html', products=products, categories=categories, shelf_locations=shelf_locations), 200)
    return render_template('index.html', products=products, categories=categories, shelf_locations=shelf_locations)

@app.route('/create_order', methods=['POST'])
def create_order():
    form = OrderForm()
    if form.validate_on_submit():
        product_id = form.product_id.data
        customer_name = form.customer_name.data
        product = Product.query.get(product_id)
        if product and product.stock > 0:
            order = Order(product_id=product_id, customer_name=customer_name)
            product.stock -= 1
            db.session.add(order)
            db.session.commit()
            return jsonify({'success': True, 'order_id': order.id})
    return jsonify({'success': False, 'message': 'Product unavailable'})

@app.route('/staff')
def staff_view():
    orders = Order.query.filter_by(status='pending').all()
    return render_template('staff.html', orders=orders)

@app.route('/complete_order/<int:order_id>', methods=['POST'])
def complete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        order.status = 'completed'
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False})

@app.route('/dashboard')
@login_required
def dashboard():
    user_orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.timestamp.desc()).all()
    # Find top categories from user's order history
    from collections import Counter
    product_ids = [order.product_id for order in user_orders]
    products = Product.query.filter(Product.id.in_(product_ids)).all() if product_ids else []
    category_counts = Counter([p.category for p in products if p.category])
    top_categories = [cat for cat, _ in category_counts.most_common(2)]
    # Recommend products from top categories, excluding already ordered
    recommended = []
    if top_categories:
        recommended = Product.query.filter(Product.category.in_(top_categories), ~Product.id.in_(product_ids)).limit(4).all()
    if not recommended:
        # Fallback: show most popular (by stock) or random products
        recommended = Product.query.order_by(Product.stock.desc()).limit(4).all()
    return render_template('dashboard.html', orders=user_orders, recommended=recommended)

@app.route('/order', methods=['POST'])
def order():
    form = OrderForm()
    try:
        if form.validate_on_submit():
            product_id = form.product_id.data
            customer_name = form.customer_name.data
            store = form.store.data
            user_id = current_user.id if current_user.is_authenticated else None
            order = Order(product_id=product_id, customer_name=customer_name, user_id=user_id, store=store)
            db.session.add(order)
            db.session.commit()
            return jsonify({'success': True, 'store': store})
        return jsonify({'success': False, 'error': 'Form validation failed'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)})

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username, is_admin=True).first()
            if user and check_password_hash(user.password_hash, password):
                session['admin_logged_in'] = True
                return redirect(url_for('admin_dashboard'))
        flash('Invalid admin credentials.')
    return render_template('admin_login.html', form=form)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    orders = Order.query.order_by(Order.timestamp.desc()).all()
    products = Product.query.order_by(Product.name).all()
    return render_template('admin_dashboard.html', orders=orders, products=products)

@app.route('/admin/add_product', methods=['GET', 'POST'])
def admin_add_product():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            shelf_location=form.shelf_location.data,
            stock=form.stock.data,
            category=form.category.data,
            high_shelf=form.high_shelf.data,
            image_url=form.image_url.data
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_product_form.html', form=form)

@app.route('/admin/edit_product/<int:product_id>', methods=['GET', 'POST'])
def admin_edit_product(product_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        form.populate_obj(product)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_product_form.html', form=form)

@app.route('/admin/delete_product/<int:product_id>')
def admin_delete_product(product_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))

def get_locale():
    from flask import session, request
    return session.get('lang', request.accept_languages.best_match(app.config['LANGUAGES']))

babel.locale_selector_func = get_locale

@app.context_processor
def inject_current_locale():
    return dict(current_locale=str(get_locale()))

@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    from flask import session, redirect, request
    session['lang'] = lang_code
    return redirect(request.referrer or '/')

if __name__ == "__main__":
    try:
        with app.app_context():
            db.create_all()
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting application: {e}")
