# config

This structure was automatically created by [Django Bootstrapper](https://pypi.org/project/django-bootstrapper/)

Default folder structure:

```text
project_folder
├── applications
│   ├── authentication (Authentication from https://github.com/contraslash/authentication-django)
│   ├── base_template (Base template from https://github.com/contraslash/template_cdn_bootstrap)
│   └── __init__.py
├── base (base from https://github.com/contraslash/base-django)
├── manage.py
└── project_name
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


## Local Usage
Be sure you have python3.7+ installed

execute

```bash
python3 -m venv cedecur_env
source ./cedecur_env/bin/activate

# or in windows
# cedecur_env\Scripts\activate.bat

# Then install the requirements
pip install -r requirements.txt
python manage.py runserver
```

You can build your container

```bash
docker build -t contraslash/cedecur .
```

## Deploy into production

To deploy into a production server, compile the docker image inside your production server and
execute the following commands modifying the values inside the interpolation strings (the ones inside ${})

```bash

docker service rm cedecur
docker service create \
    --name cedecur \
    --publish 8000:8000 \
    --env SITE_ID=2 \
    --env ENV=PRODUCTION \
    --env DEBUG=False \
    --env CONFIG_DATABASE_DATABASE=${DB_DATABASE} \
    --env CONFIG_DATABASE_USERNAME=${DB_USER} \
    --env CONFIG_DATABASE_PASSWORD=${DB_PASSWORD}" \
    --env CONFIG_DATABASE_HOST=${DB_HOSTS} \
    --env CONTROL_DATABASE_PORT=3306 \
    --mount type=bind,source=${LOCAL_MEDIAFOLDER},destination=/code/media \
    contraslash/cedecur
```
