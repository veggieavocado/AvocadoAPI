FROM python:3.6

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

COPY . /app

RUN pip3 install -q Django==1.11
RUN pip3 install -r /app/requirements.txt

ENV DJANGO_ENV=production
ENV DOCKER_CONTAINER=True

WORKDIR /app
RUN python3 manage.py makemigrations
RUN python3 manage.py makemigrations accounts
RUN python3 manage.py makemigrations contents
RUN python3 manage.py makemigrations services
RUN python3 manage.py migrate auth
RUN python3 manage.py migrate

EXPOSE 8000

CMD ["uwsgi", "--ini", "/app/config/uwsgi.ini"]
