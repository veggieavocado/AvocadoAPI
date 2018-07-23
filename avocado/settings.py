import os
import raven
from cryptography.fernet import Fernet

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
SECRET_KEY = '4w=ni_m52itcdzl6h1zl4+!0de6-4#qt%nl04xvx%x5(a-$slw'

##### 새팅 상태 위에서 먼저 정의 #####
# 민감한 정보 불러오기: 아이피 주소
testing = os.environ.get('TRAVIS', 'False') # Travis에서 작동하는지 확인
django_env = os.environ.get('DJANGO_ENV', 'local') # 도커에서 작동하는지 확인
###############################

if testing == 'True':
    # Travis 테스트 작동 중이면, 시크릿 키가 없기 때문에 비밀 환경변수 사용
    KEY = os.environ['KEY']
else:
    from avocado.crypt_key import KEY

KEY = KEY.encode() # 스트링값 바이트로 변경
cipher_suite = Fernet(KEY)

ciphered_ip = b'gAAAAABbUuztdRPMIpZ9l9Qgh7P-egEEHEHhEcm05nJpAzQi-4rCXDXZGp9rdjFultU8okqISgemKA_Tn6G8pdKlOCZweL40dg=='
IP_ADDRESS = cipher_suite.decrypt(ciphered_ip).decode()

ALLOWED_HOSTS = ['127.0.0.1', '127.0.1.1', IP_ADDRESS]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # corsheaders
    'corsheaders',

    # Sentry: 에러 로깅
    'raven.contrib.django.raven_compat',

    # Django Restframework (API Template)
    'rest_framework',

    # 우박 앱
    'accounts',
    'services',
]

### Sentry 새팅 ###
RAVEN_CONFIG = {
    'dsn': 'https://507fdfd441ad48eab52ea30f861d47b7:97b0e0ea6ce44ca1be336fa6edba9d76@sentry.io/1247366',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(BASE_DIR),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'avocado.urls'

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

WSGI_APPLICATION = 'avocado.wsgi.application'

# 로컬에서는 도커 링크를 통한 연결을 시도하고,

### 서버: PostgreSQL 사용 ###
### Travis CI 혹은 로컬: sqlite3을 사용 ###
if testing == 'True' or django_env == 'local':
    print('USING SQLITE3, NOT PRODUCTION')
    database_option = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif django_env == 'production':
    database_option = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'avocado',
            'USER': 'avocado',
            'PASSWORD': 'veggieavocado2018',
            'HOST': IP_ADDRESS,
            'PORT': 5432,
        }
    }

DATABASES = database_option

### 서버 Redis 사용 ###
if testing == 'True' or django_env == 'local':
    ### 실제 서비스 중에만 캐시 서버 사용 ###
    print('NO CACHE, NOT PRODUCTION')
elif django_env == 'production':
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://cache:6379/1", # 1번 DB
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
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

### API 서버라 static은 필요없지만, rest framework에서 디버깅 용으로 사용이 필요하기 때문에 추가 ###
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static-dist/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

# https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True # 외부에서 API 요청 가능하도록 새팅

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

# ## 만약 도커에서 작동한다면, 서버에서 돌아가고 있기 때문에 API 결과를 json형식으로 리턴해야 한다.
# if django_env == 'production':
#     REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ('rest_framework.renderers.JSONRenderer',)
