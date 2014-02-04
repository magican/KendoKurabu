
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "142428ca-22a1-4917-8495-d1a728dd6252f2001b2d-df81-4ed3-b464-0c71ea504a324ba7ca3e-c6ea-493f-ad2c-8475cbf2448e"
NEVERCACHE_KEY = "2a2978fd-77e8-4722-8885-c50ba57278ef7e5e6290-d726-4ec5-bf97-65dc4c38acbc872cb916-5d70-43e0-a432-f378958eb03f"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
