# Portfolio - API
The purpose of this site is to expose my individual and professional projects related to web development, thus demonstrating my knowledge and skills, easy access to potential recruiters to my resume and point of contact.

#### DEPLOYED BACKEND API [LINK](https://drf-api-coffeeie.herokuapp.com/)
#### DEPLOYED FRONTEND [LINK - LIVE SITE](https://coffeeie-p5.herokuapp.com/)
#### DEPLOYED FRONTEND [REPOSITORY](https://github.com/PEmbarach/coffeeie)

## Table of Contents
+ [User Stories](#user-stories "User Stories")
+ [Database](#database "Database")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

## User Stories:
I have included links to the [GitHub Issues](https://github.com/PEmbarach/coffeeie/issues) for this project, as well as the [KANBAN board](https://github.com/users/PEmbarach/projects/6/views/1).

## Database:
![SQL Database model](/static/readme_images/diagram_ER.png)

## Testing:
### Validator Testing: 
All python files passed through the PEP8 validator with no issues, apart from some long-line errors which were rectifed. Few long-line error remains in settings.py (line 120, 163, 166, 169 and 172):  [PEP8](https://pep8ci.herokuapp.com/).

![PEP8](/static/readme_images/PEP8_Settings.png)

### Manual Testing:
1. Manually verified each url path created works & opens without error.
2. Verified that the CRUD functionality is available in each app via the development version: Comments, Contact, Followers, Likes, Posts and Profile.
 - Checked this by going to each link.
 - Creating a new item.
 - Checking new item URL path. 
 - Editing the item (not available for Likes, Followers or Users)
 - Deleting the item (Not available for Users or Profiles)
3. Ensured search feature for Posts, User, Location and Price apps returns results. 

### Unfixed Bugs
- None so far.

## Technologies Used:
### Main Languages Used:
- Python

### Frameworks, Libraries & Programs Used:
- Django
- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers


## Deployment:
### Project creation:
1. Create the GitHub repository.
2. Create the project app on [Heroku](heroku.com).
3. Add the Postgres package to the Heroku app via the Resources tab.
4. Once the GitHub repository was launched on GitPod, installed the following packages using the `pip install` command:
```
'django<4'
dj3-cloudinary-storage
Pillow
djangorestframework
django-filter
dj-rest-auth
'dj-rest-auth[with_social]'
djangorestframework-simplejwt
dj_database_url psycopg2
gunicorn
django-cors-headers
```
5. Created the Django project with the following command:
```
django-admin startproject project_name .
```
6. Navigated back to [Heroku](heroku.com), and under the Settings tab, added the following configvars:
 - Key: SECRET_KEY | Value: hidden
 - Key: CLOUDINARY_URL | Value: cloudinary://hidden
 - Key: DISABLE_COLLECTSTATIC | Value: 1
 - Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com
7. Add two additional configvars once the ReactApp has been created:
 - Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
 - Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io
  - Check that the trailing slash `\` at the end of both links has been removed.
  - Gitpod occasionally updates the browser preview link. Should this occur, the CLIENT_ORIGIN_DEV value shall need to be updated.

8. Created the env.py file, and added the following variables. The value for DATABASE_URL was obtained from the Heroku configvars in the previous step:
```
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://hidden'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'hidden'
os.environ['DATABASE_URL'] = 'postgres://hidden'
```
### In settings.py: 
<!-- For reference, refer to: [DRF-API walkthrough settings.py](https://github.com/Code-Institute-Solutions/drf-api/blob/2c0931a2b569704f96c646555b0bee2a4d883f01/drf_api/settings.py) -->
9. Add the following to INSTALLED_APPS to support the newly installed packages:
```
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
'rest_framework',
'django_filters',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
'corsheaders',
```
10. Import the database, the regular expression module & the env.py
```
from pathlib import Path
import os
import dj_database_url
import re


if os.path.exists('env.py'):
    import env
```

11. Below the import statements, add the following variable for Cloudinary:
```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
```
- Below INSTALLED_APPS, set site ID:
```
SITE_ID = 1
```
12. Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```
13. Set the default renderer to JSON:
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
14. Beneath that, added the following:
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```
15. Then added:
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```
16. Updated DEBUG variable to:
```
DEBUG = True
```
17. Updated the DATABASES variable to:
```
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
}
```
18. Added the Heroku app to the ALLOWED_HOSTS variable:
```
os.environ.get('ALLOWED_HOST'),
'localhost',
```
19. Below ALLOWED_HOST, added the CORS_ALLOWED variable as shown in [DRF-API walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/a6250c9e9b284dbf99e53ac8e8b68d3e/0c9a4768eea44c38b06d6474ad21cf75/?child=first):
```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
20. Also added to the top of MIDDLEWARE:
```
'corsheaders.middleware.CorsMiddleware',
```
- During a deployment issue, it was suggested by a fellow student, Johan, to add the following lines of code below CORS_ALLOW_CREDENTIALS:
```
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CSRF_TRUSTED_ORIGINS = [os.environ.get(
    'CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN',
)]
```
- In addition, Johan also suggested to add the following import statement at the top of the settings.py file:
```
from corsheaders.defaults import default_headers, default_methods
```

### Final requirements:
21. Created a Procfile, & added the following two lines:
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi
```
22. Migrated the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
23. Froze requirements:
```
pip3 freeze --local > requirements.txt
```
24. Added, committed & pushed the changes to GitHub
25. Navigated back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.
26. Deployed the branch.


## CREDITS:

### Content:
- The creation of this API database was provided through the step by step guide of the C.I. DRF-API walkthrough project.
- All classes & functions have been credited.
- Modifications have been made to the 'Posts' app models, and an additional one apps along with models, serializers & views have been created by me.


### Media:
- The Default Profile Image was used provided by CI during the course [Default Profile Image](https://codeinstitute.s3.amazonaws.com/ReactEssentials/DRF/Images/default_profile.jpg)
- Default Post image from [Default Post Image](https://codeinstitute.s3.amazonaws.com/ReactEssentials/DRF/Images/default_post.jpg)
