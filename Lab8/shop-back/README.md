# shop-back

Django backend API for the Online Shop

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate 

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
