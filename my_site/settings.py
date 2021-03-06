"""
Django settings for my_site project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7l99hsct1+^t-z_8#9fz(@w-4j)gs2g_%^02_1!nu$nu&qm-5x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'message',
    'announcement',
    'xadmin',
    'crispy_forms',
    'captcha',
    'users',
    'schoolinfo',
    'thesis',
    'student',
    'teacher',
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

ROOT_URLCONF = 'my_site.urls'

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

WSGI_APPLICATION = 'my_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cms_site_db',
        'USER': 'zjj',
        'PASSWORD': 'zjjpassword',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

AUTH_USER_MODEL = 'users.User'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
UPLOAD_DIR = os.path.join(MEDIA_ROOT, 'upload')  #D:\1毕业设计\media\upload
PUBLIC_DIR = os.path.join(MEDIA_ROOT, 'public')  #D:\1毕业设计\media\public

#富文本编辑框
CKEDITOR_CONFIGS = { 
    'default':{},
    'thesisContent_ckeditor':{ 
        'toolbar':'custom',
        'toolbar_custom':[
            {'name':'styles ','items':['Format','Font','FontSize']},
            {'name':'editing', 'items': ['Find', 'Replace']},
            {'name':'basicstyles',
             'items':['Bold','Italic','Underline','RemoveFormat']},
            {'name':'paragraph',
             'items':['NumberedList','BulletedList']},
            {'name':'colors', 'items': ['TextColor', 'BGColor']},
        ],
        'font-size': '16px',
        'height': '250',
        'width': 'auto',
        'tabSpaces': 4,   #设置tab键为多少空格
        'removePlugins': 'elementspath',  #去除编辑框最下部提示
        'resize_enabled':False,        #去除编辑框最下部
    },
}

#创建数据库缓存
CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

#设置验证码输入框的显示格式
CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s %(hidden_field)s %(image)s'

