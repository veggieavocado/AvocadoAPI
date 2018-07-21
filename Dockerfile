FROM python:3.6

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

COPY . /app

RUN pip3 install -r /app/requirements.txt

ENV DJANGO_ENV=production
ENV DOCKER_CONTAINER=True

EXPOSE 8000

CMD ["uwsgi", "--ini", "/app/config/uwsgi.ini"]
