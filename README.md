# Grocery AI Backend (Minimal)

A minimal Django REST API for grocery stores with simple AI stubs (forecast + categorization).

## Run locally

```bash
python -m venv venv
venv\\Scripts\\activate  # Windows
source venv/bin/activate # Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Then visit http://127.0.0.1:8000/
