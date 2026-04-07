import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
django.setup()

from django.contrib.auth import get_user_model
from api.models import Category, Product

# Superuser
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
    print('Superuser created: admin / admin1234')
else:
    print('Superuser already exists')

# Categories (6 total, last 2 are empty)
categories_data = ['Electronics', 'Clothing', 'Books', 'Sports', 'Toys', 'Garden']
categories = {}
for name in categories_data:
    cat, created = Category.objects.get_or_create(name=name)
    categories[name] = cat
    print(f'Category: {name}')

# Products
products_data = [
    ('iPhone 15', 999.99, 'Latest Apple smartphone', 10, True, 'Electronics'),
    ('Samsung Galaxy S24', 849.99, 'Android flagship phone', 15, True, 'Electronics'),
    ('MacBook Pro', 1999.99, 'Apple laptop with M3 chip', 5, True, 'Electronics'),
    ('Sony WH-1000XM5', 349.99, 'Noise cancelling headphones', 20, True, 'Electronics'),
    ('iPad Air', 599.99, 'Apple tablet', 8, True, 'Electronics'),
    ('Nike Air Max', 129.99, 'Classic running shoes', 30, True, 'Clothing'),
    ('Adidas Hoodie', 79.99, 'Comfortable cotton hoodie', 25, True, 'Clothing'),
    ('Levi\'s Jeans 501', 89.99, 'Classic straight fit jeans', 40, True, 'Clothing'),
    ('Zara T-Shirt', 29.99, 'Basic white t-shirt', 50, True, 'Clothing'),
    ('The North Face Jacket', 199.99, 'Waterproof winter jacket', 12, True, 'Clothing'),
    ('The Great Gatsby', 12.99, 'F. Scott Fitzgerald classic novel', 100, True, 'Books'),
    ('Clean Code', 34.99, 'A handbook of agile software craftsmanship', 35, True, 'Books'),
    ('Harry Potter Box Set', 59.99, 'Complete 7-book collection', 20, True, 'Books'),
    ('1984', 10.99, 'George Orwell dystopian novel', 80, True, 'Books'),
    ('Python Crash Course', 29.99, 'Beginner programming book', 45, True, 'Books'),
    ('Yoga Mat', 39.99, 'Non-slip exercise mat', 60, True, 'Sports'),
    ('Dumbbells Set', 89.99, 'Adjustable 2-20kg dumbbell set', 15, True, 'Sports'),
    ('Basketball', 49.99, 'Official size basketball', 25, True, 'Sports'),
    ('Tennis Racket', 79.99, 'Professional tennis racket', 18, True, 'Sports'),
    ('Cycling Helmet', 59.99, 'Lightweight safety helmet', 22, True, 'Sports'),
]

for name, price, description, count, is_active, cat_name in products_data:
    product, created = Product.objects.get_or_create(
        name=name,
        defaults={
            'price': price,
            'description': description,
            'count': count,
            'is_active': is_active,
            'category': categories[cat_name],
        }
    )
    print(f'Product: {name}')

print('\nDone! Go to http://127.0.0.1:8000/admin/ and login with admin / admin1234')
