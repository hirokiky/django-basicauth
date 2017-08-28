import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=['testserver'],
    DATABASES={"default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:"
    }},
    ROOT_URLCONF='tests.testing_urls',
)
django.setup()
