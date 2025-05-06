import unittest
from app import app, db, Product, User
from flask import url_for
from werkzeug.security import generate_password_hash

class ShelfHelperTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
            # Create a test user
            user = User(username='testuser', email='test@example.com', password_hash=generate_password_hash('testpass'))
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.app.post('/register', data={
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123'
        }, follow_redirects=True)
        self.assertIn(b'Registration successful', response.data)

    def test_login_logout(self):
        response = self.app.post('/login', data={
            'username': 'testuser',
            'password': 'testpass'
        }, follow_redirects=True)
        self.assertIn(b'Logout', response.data)
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'Logged out successfully', response.data)

    def test_add_product(self):
        with app.app_context():
            product = Product(name='Widget', description='A test widget', price=9.99, stock=10)
            db.session.add(product)
            db.session.commit()
            self.assertIsNotNone(Product.query.filter_by(name='Widget').first())

    def test_order_creation(self):
        with app.app_context():
            product = Product(name='Widget', description='A test widget', price=9.99, stock=10)
            db.session.add(product)
            db.session.commit()
            response = self.app.post('/order', data={
                'product_id': product.id,
                'customer_name': 'Test Customer',
                'store': 'Walmart'
            }, follow_redirects=True)
            self.assertIn(b'success', response.data)

if __name__ == '__main__':
    unittest.main()
