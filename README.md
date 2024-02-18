to run project:

1. install poetry - `pip install poetry`
2. install dependencies - `poetry install --no-root`
3. setup DB of project - `python manage.py migrate`
4. run project - `python manage.py runserver`
5. you can access:
   http://127.0.0.1:8000/api/import/ - for importing data
   http://127.0.0.1:8000/api/detail/{model_name}/ - for getting list of data
   http://127.0.0.1:8000/api/detail/{model_name}/{model_id}/ - for data detail view
