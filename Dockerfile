FROM python:3.6

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

COPY . /app

RUN pip3 install -r /app/requirements.txt

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000

CMD ["uwsgi", "--ini", "/app/config/uwsgi.ini"]
