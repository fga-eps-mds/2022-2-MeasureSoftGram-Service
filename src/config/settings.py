"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    'django-insecure-9(nkl$g75ia=@q3p*s83rc9y=q5=!q@kr8+s3*xc-t441#jmg%'

)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "t", "1")

ALLOWED_HOSTS = ['*']

# Allowed origins on CORS
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://measuresoftgram.herokuapp.com',
    'http://measuresoftgram.herokuapp.com',
    'https://stg-measuresoftgram.herokuapp.com',
    'http://stg-measuresoftgram.herokuapp.com',
]


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'simple_history',
    'corsheaders',
    'debug_toolbar',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
]

APPLICATION_APPS = [
    'accounts',
    'organizations',

    'metrics',
    'measures',
    'subcharacteristics',
    'characteristics',
    'sqc',

    'pre_configs',
    'goals',
    'entity_trees',

    'collectors',

    'utils',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + APPLICATION_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "0.0.0.0")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORE_URL = os.getenv("CORE_URL", "http://localhost:5000")

django_heroku.settings(locals())

# Django Rest Framework config
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 500,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# allauth related configs
SITE_ID = int(os.getenv("SITE_ID", "1"))

LOGIN_REDIRECT_URL = os.getenv("LOGIN_REDIRECT_URL", "127.0.0.1:8080")

CREATE_FAKE_DATA = os.getenv(
    "CREATE_FAKE_DATA", "False"
).lower() in ("true", "t", "1")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

GITHUB_ISSUE_METRICS_THRESHOLD = int(
    os.getenv("GITHUB_ISSUE_METRICS_THRESHOLD", "7")
)

MAXIMUM_NUMBER_OF_HISTORICAL_RECORDS = int(os.getenv(
    "MAXIMUM_NUMBER_OF_HISTORICAL_RECORDS",
    "100",
))

GITHUB_PIPELINE_METRICS_THRESHOLD = int(
    os.getenv("GITHUB_PIPELINE_METRICS_THRESHOLD", "90")
)

DATA_UPLOAD_MAX_NUMBER_FIELDS = int(os.getenv(
    "DATA_UPLOAD_MAX_NUMBER_FIELDS",
    "100000",
))

AUTH_USER_MODEL = "accounts.CustomUser"

if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

GITHUB_METRICS = [
    {
        "key": "number_of_resolved_issues_in_the_last_x_days",
        "name": "Number of resolved issues in the last x days",
        "metric_type": "INT",
        'api_params': [
            'issues_repository_url',
            'issues_metrics_x_days',
        ],
        'methods_params_map': {
            '__init__': {
                'url': 'issues_repository_url',
                'token': 'github_token',
            },
            'metric_method': {
                'method_name': 'get_number_of_issues_resolved_in_the_last_x_days',
                'method_params': {
                    'x': 'issues_metrics_x_days',
                }
            }
        },
    },
    {
        "key": "number_of_resolved_issues_with_US_label_in_the_last_x_days",
        "name": "Number of resolved issues with US label in the last x days",
        "metric_type": "INT",
        'api_params': [
            'issues_repository_url',
            'issues_metrics_x_days',
            'user_story_label',
        ],
        'methods_params_map': {
            '__init__': {
                'url': 'issues_repository_url',
                'token': 'github_token',
            },
            'metric_method': {
                'method_name': 'get_number_of_issues_resolved_in_the_last_x_days',
                'method_params': {
                    'x': 'issues_metrics_x_days',
                    'label': 'user_story_label',
                }
            }
        },
    },
    {
        "key": "number_of_issues_with_bug_label_in_the_last_x_days",
        "name": "Number of issues with bug label in the last x days",
        "metric_type": "INT",
        "api_params": [
            'issues_repository_url',
            'issues_metrics_x_days',
            'bug_label',
        ],
        'methods_params_map': {
            '__init__': {
                'url': 'issues_repository_url',
                'token': 'github_token',
            },
            'metric_method': {
                'method_name': 'get_total_number_of_issues_in_the_last_x_days',
                'method_params': {
                    'x': 'issues_metrics_x_days',
                    'label': 'bug_label',
                }
            }
        },
    },
    {
        "key": "total_number_of_issues_with_US_label_in_the_last_x_days",
        "name": "Total number of issues with US label in the last x days",
        "metric_type": "INT",
        "api_params": [
            'issues_repository_url',
            'issues_metrics_x_days',
            'user_story_label',
        ],
        'methods_params_map': {
            '__init__': {
                'url': 'issues_repository_url',
                'token': 'github_token',
            },
            'metric_method': {
                'method_name': 'get_total_number_of_issues_in_the_last_x_days',
                'method_params': {
                    'x': 'issues_metrics_x_days',
                    'label': 'user_story_label',
                }
            }
        },
    },
    {
        "key": "total_number_of_issues_in_the_last_x_days",
        "name": "Total number of issues in the last x days",
        "metric_type": "INT",
        "api_params": [
            'issues_repository_url',
            'issues_metrics_x_days',
        ],
        'methods_params_map': {
            '__init__': {
                'url': 'issues_repository_url',
                'token': 'github_token',
            },
            'metric_method': {
                'method_name': 'get_total_number_of_issues_in_the_last_x_days',
                'method_params': {
                    'x': 'issues_metrics_x_days',
                }
            }
        },
    },
    {
        "key": "number_of_build_pipelines_in_the_last_x_days",
        "name": "Number of build pipelines in the last x days",
        "metric_type": "INT",
        "api_params": [
            'pipelines_repository_url',
            'pipeline_metrics_x_days',
            'build_pipeline_names',
        ],
        'methods_params_map': {
            '__init__': {
                'url': 'pipelines_repository_url',
                'token': 'github_token',
            },
            'metric_method': {
                'method_name': 'get_the_number_of_build_pipelines_executed_in_the_last_x_days',
                'method_params': {
                    'x': 'issues_metrics_x_days',
                    'build_pipeline_names': 'build_pipeline_names',
                },
            },
        },
    },
    {
        "key": "runtime_sum_of_build_pipelines_in_the_last_x_days",
        "name": "Runtime sum of build pipelines in the last x days",
        "metric_type": "INT",
        "api_params": [
            'pipelines_repository_url',
            'pipeline_metrics_x_days',
            'build_pipeline_names',
        ],
        'methods_params_map': {
            '__init__': {
                'url': 'pipelines_repository_url',
                'token': 'github_token',
            },
            'metric_method': {
                'method_name': 'get_the_sum_of_their_durations_in_the_last_x_days',
                'method_params': {
                    'x': 'issues_metrics_x_days',
                    'build_pipeline_names': 'build_pipeline_names',
                },
            },
        },
    },
]
