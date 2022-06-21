# Landing webpage
Written in Python, Django with JavaScript.
It sends learning materials to the user after watching and embeded youtube video.
Available under https://darmowamapka.pl url.

# installation & configuration
To get the website working on local you need to do few things:
  - create new django project
  - fork the project and paste it in yours new project's directory
  - install required packages
  - modify settings.py
  - makemgirations & migrate
  
We will skip creating new project and forking this one.

* installing required packages
  After pasting project files into your new django project you should have file 'requirements.txt' which contains names and versions of required packages.
  To install it, in your terminal:  
  `pip install -r requirements.txt`

* modifying settings.py
  - At first, you have to add `main`, `phonenumber_field` and `django_cleanup.apps.CleanupConfig` app in `INSTALLED_APPS`:
    ```
    INSTALLED_APPS = [
      ...
      'main',
      'phonenumber_field',
      'django_cleanup.apps.CleanupConfig'
    ]
    ```
  - then, you have to initiate these variables with email host information to get the email sending working
      ```
      EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
      EMAIL_HOST = <email host>
      EMAIL_HOST_USER = <email address>
      EMAIL_HOST_PASSWORD = <password>
      EMAIL_PORT = <email_port>
      EMAIL_USE_SSL = <True/False/
      DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
      ```
  - lastly, specify static and media files directories. For this project it will be:
    ```
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
    MEDIA_DIR = ''
    ```
* makemigrations & migrate
  - in your terminal, in project's root directory:  
  `python manage.py makemigrations`  
  `python manage.py migrate`  
  Now you can run the server  
  `python manage.py runserver`
