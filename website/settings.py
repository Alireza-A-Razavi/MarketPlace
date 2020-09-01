import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r&l5m&!!ne%yjv=^r5t4vpb!o0(z-#(bei2^o8)o@ung8swi^z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'users.apps.UsersConfig',
    'categories.apps.CategoriesConfig',
    'blog.apps.BlogConfig',
    'merchandise.apps.MerchandiseConfig',
    'products.apps.ProductsConfig',


    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',

    'tinymce',
    'hitcount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'damir',
#         'USER': 'jeremih',
#         'PASSWORD': 'hellomother',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


AUTH_USER_MODEL = 'users.User'





EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CSRF_COOKIE_NAME = "csrftoken"

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'users.serializers.CustomRegisterSerializer',
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',
    'TOKEN_SERIALIZER': 'users.serializers.TokenSerializer'
}

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.AllowAny',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#
#     ),
# }
#
# # REST_FRAMEWORK = {
# #     'DEFAULT_AUTHENTICATION_CLASSES': [
# #         'rest_framework.authentication.BasicAuthentication',
# #         'rest_framework.authentication.SessionAuthentication',
# #     ]
# # }
# #
# #
# #
# # AUTHENTICATION_BACKENDS = [
# #     # Needed to login by username in Django admin, regardless of `allauth`
# #     'django.contrib.auth.backends.ModelBackend',
# #
# #     # `allauth` specific authentication methods, such as login by e-mail
# #     'allauth.account.auth_backends.AuthenticationBackend',
# # ]


SITE_ID = 1

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# # Vue project location
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend/damdam')

# # Vue assets directory (assetsDir)
STATICFILES_DIRS = [
    os.path.join(FRONTEND_DIR, 'js'),
    os.path.join(FRONTEND_DIR, 'public'),
    os.path.join(FRONTEND_DIR, 'views'),
    os.path.join(FRONTEND_DIR),
]

# # Webpack output location containing Vue index.html file (outputDir)
TEMPLATES[0]['DIRS'] += [
    os.path.join(FRONTEND_DIR, 'views'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')


ACCOUNT_FORMS = {'signup': 'users.forms.CustomSignUpForm'}
