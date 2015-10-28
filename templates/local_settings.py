
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{{service_db_engine}}', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{service_name}}',                      # Or path to database file if using sqlite3.
        # 'NAME': os.path.join(PROJECT_ROOT, 'data.db'),                      # Or path to database file if using sqlite3.
        'USER': '{{service_name}}',                      # Not used with sqlite3.
        'PASSWORD': '{{service_db_password}}',                  # Not used with sqlite3.
        'HOST': '{{service_db_host}}',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

STATIC_ROOT = '/srv/static/{{service_name}}/static/'

{% for service in services %}
{{service|upper}}_BASE_URL = "http://{{service}}.{{tld}}"
{% endfor %}

TANGENT_ADMIN_TOKEN='{{tangent_admin_token}}'
TLD='{{tld}}'
