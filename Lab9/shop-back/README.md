# shop-back

Django REST Framework backend API for Online Shop

## Setup

```bash
python -m venv venv
venv\Scripts\activate  

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata initial_data
python manage.py createsuperuser
python manage.py runserver
```