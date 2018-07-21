import os
import raven

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '(1*))8!e15ouzj635vf&of1l#x)n%w!hiw2k@!^rnq8sv!zssx'
ALLOWED_HOSTS = ['127.0.0.1', '127.0.1.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'rest_framework',

    'api',
]

try:
    # TRAVIS 환경변수를 들고와서 testing 변수에 넣어주기
    # 환경변수가 없어서 에러가 발생하면 testing을 'False'로 세팅
    testing = os.environ['TRAVIS']
    DEBUG = True
except:
    testing = 'False'

if testing == 'False':
    INSTALLED_APPS.append('configs') # Travis CI 테스팅 때는 config없이 돌아갈 수 있도록 설정

    from configs.base import CONFIG, THIS_SYSTEM
    if CONFIG['common']['DEBUG'] == 'True':
        DEBUG = True
    else:
        DEBUG = False
    # add Sentry settings here
    # Sentry도 마찬가지로 Travis CI에서는 필요없음
    RAVEN_CONFIG = {
        'dsn': CONFIG['common']['SENTRY_URL'],
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
    }

    if THIS_SYSTEM == 'web':
        ALLOWED_HOSTS.append(CONFIG['ip-address']['web'])

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'woobak.urls'

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

                'templates.context_processors.ga_tracking_id',
                'templates.context_processors.use_ga',
            ],
        },
    },
]

WSGI_APPLICATION = 'woobak.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static-dist/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

GA_TRACKING_ID = 'UA-122243187-1'
if DEBUG == True: # 로컬/개발용은 트래킹 안 하기
    # 하지만 현재는 모두 개발 중이므로, 구글 애널리틱스 적용시키기
    USE_GA = True
else:
    USE_GA = False

# djangorestframework-jwt
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
