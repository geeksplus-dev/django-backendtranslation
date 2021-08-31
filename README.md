=====
Translation
=====

translation is a Django app works with i18next when translation is being stored in the database, it retrieves required translations from database,
and store missing keys sent from from frontend .

## Quick start

1. Install via pip into a virtualenv:

```bash
    pip3 install git+https://github.com/geeksplus-dev/django-backendtranslation.git
```

2. Add "translation" to your INSTALLED_APPS setting like this::

```python
   INSTALLED_APPS = [
   ...
   'translation',
   ]
```

3. Include the translation URLconf in your project urls.py like this::

```python
   path('translation/', include('translation.urls')),
```

4. Run `python manage.py migrate` to create the translation tables in the database.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a translations (you'll need the Admin app enabled).

6. In case you want to change or extend app models, after making the desired changes run:

```bash
   python make_migrations.py
```
