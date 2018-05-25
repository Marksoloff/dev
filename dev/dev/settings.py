"""
Django settings for dev project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# image code below
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dev/static/')
]


MEDIA_URL = "/media/"
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, "/media/")

#dictionaries of prompts & responses used in hhbg
prompts = {
    "postStat": "Lookin' good, ya filthy animal! Now let's put a name to dat face.",
    "diyNameQuestion": "Ready to generate your bear name? Or do you wanna think up your own?",
    "writeName": "Now we're cookin' with gas! Enter your bear name:",
    "preparingName": "Hit ENTER again and I'll cook up a real crackerjack name for ya.",
    "hasGenderQuestion": "Is your bear male or female? M/F?",
    "wrongGenderAnswer": "What's that? Stop bein' a mook and type 'M' or 'F'!",
    "isThereGender": "Ey, I been wonderin'... Does your bear have a gender?: Y/N?",
    "rollPrompt": "Press ENTER to create a new character, capeesh?",
    "yOrN": "I don't understand you, kid. Just type 'Y' or 'N' already!",
    "proceed": "Okee doke! Let's proceed.",
    "welcome": "Welcome to da Honey Heist Bearacter Generator",
}
responses = {
    "intro": "Welcome to da Honey Heist Bearacter Generator",
    "congrats": "Mazel tov, kid.",
    "proceed": "Okee doke! Let's proceed.",
    "baddaBoom": "Badda-BOOM! Hey get a load of you, ya stinkin': ",
    "meetchaTyped": "Nice ta meetcha, ",
    "yourNameIs": "And your name is: ",
    "welcomeGang": "Welcome to the gang!",
    "meetMale": "Nice to meetcha, pal!",
    "meetFem": "Pleased to meetcha miss. Charmed, I'm sure.",
    "genRetort": "Ah, what's gender anyways but a social construct?",
}
#name and stat variables used in hhbg
boy_name = ("Bugsy", "Artie", "Mooksie", "Petey", "Vinnie", "Lou", "Mungo", "Mack", "Tony", "Teddy", "Bobo", "Chucky", "Bobby", "Lucio", "Musky", "Sticks", "Clawsy", "Yogi")
girl_name = ("Ursula", "Coco", "Wendy", "Velvet", "Betty", "Mama", "Louisa", "Belladonna", "Carmen", "Jaimie", "Veronica", "Squeaky", "Bang-Bang", "Cookies", "Delores")
asex_name = ("Grumbles", "Pork-Bone", "Pittsburgh", "Brumbo", "Binky", "Stabs", "Punchy", "Husky", "Shortstack", "Pookie", "Bing Bing", "Clawsy", "Dead-eye", "Knuckles", "Mookie", "Sneaky", "Two-toes", "Shades", "Bully", "Meatsy", "Chuckles", "Bingo", "Pathos")
surname = ("Malone", "LeRoy", "Falcone", "O'Malley", "Pitsacotta", "Rourke", "Putanesca", "the Chopper", "MacKenzie", "the Knife", "Fujimura", "Tanaka", "the Vermin of Scarsdale")

personalities = ("Rookie", "Washed up", "Retired", "Unhinged", "Slick", "Incompetent")
bear_types = ("Grizzly Bear", "Polar Bear", "Panda", "Black Bear", "Sun Bear", "Honey Badger")
criminal_roles = ("Enforcer", "Mastermind", "Getaway Driver", "Hacker", "Thief", "Face")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
import sys 

def find_or_create_secret_key():
    """ 
    Look for secret_key.py and return the SECRET_KEY entry in it if the file exists.
    Otherwise, generate a new secret key, save it in secret_key.py, and return the key.
    """
    SECRET_KEY_DIR = os.path.dirname(__file__)
    SECRET_KEY_FILEPATH = os.path.join(SECRET_KEY_DIR, 'secret_key.py') 
    sys.path.insert(1,SECRET_KEY_DIR) 

    if os.path.isfile(SECRET_KEY_FILEPATH):
        from secret_key import SECRET_KEY
        return SECRET_KEY
    else:
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&amp;*(-_=+)'
        new_key = get_random_string(50, chars)
        with open(SECRET_KEY_FILEPATH, 'w') as f:
            f.write("# Django secret key\n# Do NOT check this into version control.\n\nSECRET_KEY = '%s'\n" % new_key)
        from secret_key import SECRET_KEY
        return SECRET_KEY

# Make this unique, and don't share it with anybody.
SECRET_KEY = find_or_create_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bulba.apps.BulbaConfig',
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

ROOT_URLCONF = 'dev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'dev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
