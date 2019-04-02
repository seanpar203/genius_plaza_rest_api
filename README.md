# Genius Plaza Rest API
A simple rest api that revolves around recipes, ingredients & steps.

The SQLite DB is uploaded to this repo which already has 2 users with PKs 1 and 2 to allow hitting the API endpoints
without having to create a user via `python manage.py createsuperuser` or anything.

# Endpoints

1. `/api/cooking/recipes` - List & Create Endpoint
2. `/api/cooking/recipes/<int:pk>` - Detail, Update, Delete Endpoint

The Create endpoint allows passing `ingredients` and `steps` as part of creating a recipe which is more optimal than multiple round trips. 