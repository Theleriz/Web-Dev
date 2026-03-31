# shop-back

Django backend API for the Online Shop (Lab 8).

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 4. Load initial data
python manage.py loaddata initial_data

# 5. Run the server
python manage.py runserver
```

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /api/products/` | List of all Products |
| `GET /api/products/<id>/` | Get one Product by ID |
| `GET /api/categories/` | List of all Categories |
| `GET /api/categories/<id>/` | Get one Category by ID |
| `GET /api/categories/<id>/products/` | List of Products by Category |

## Project Structure

```
shop-back/
├── shop_back/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api/                # Django app
│   ├── models.py       # Product & Category models
│   ├── views.py        # API views
│   ├── urls.py         # URL patterns
│   ├── admin.py
│   └── fixtures/
│       └── initial_data.json
├── manage.py
├── requirements.txt
└── .gitignore
```
