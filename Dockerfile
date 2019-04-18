FROM contraslash/alpine-django-deploy-common

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
ADD . /code/
EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]
