# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$!x^%l^bdf9u71y#hfrunn-0*=(b(f!x4a=kkj+)1#q4()x8=@'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'ARCHeesecake$$08'
    }
}
