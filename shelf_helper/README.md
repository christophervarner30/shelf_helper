# Shelf Helper Application

A web-based application to help customers order items from high shelves in stores.

## Setup Instructions

1. Install Python requirements:
```
pip install -r requirements.txt
```

2. Run the application:
```
python app.py
```

3. Access the application:
- Customer interface: http://localhost:5000
- Staff interface: http://localhost:5000/staff

## Features

### Customer Interface
- Browse available products
- Select items for pickup
- Provide name for order identification
- Receive confirmation when order is placed

### Staff Interface
- View pending orders
- See product shelf locations
- Mark orders as complete when items are retrieved
- Real-time updates

## Initial Setup

The database will be automatically created when you first run the application. To add products, you can use the Python shell:

```python
from app import app, db, Product
with app.app_context():
    # Add sample products
    product = Product(
        name="Sample Product",
        description="Description",
        price=9.99,
        shelf_location="A1",
        stock=10
    )
    db.session.add(product)
    db.session.commit()
```
