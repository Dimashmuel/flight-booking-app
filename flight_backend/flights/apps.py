from django.apps import AppConfig

class FlightsConfig(AppConfig):
    # Default type for auto-generated primary keys (from Django 3.2+)
    default_auto_field = 'django.db.models.BigAutoField'

    # Name of the app as registered in the project
    name = 'flights'
