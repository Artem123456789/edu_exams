FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get install -y build-essential && \
    apt-get install -y libpq-dev && \
    apt-get install -y gettext && \
    apt-get -y install libev-dev && \
    apt-get -y install gcc && \
    apt-get install -y htop && \
    apt-get install -y git

WORKDIR /project

COPY ./requirements.txt requirements.txt
RUN pip install --default-timeout=1000 -r /project/requirements.txt

COPY ./docker/scripts/run_django.sh /scripts/run_django.sh
RUN sed -i 's/\r$//g' /scripts/run_django.sh
RUN chmod +x /scripts/run_django.sh

COPY ./docker/scripts/entrypoint.sh /scripts/entrypoint.sh
RUN sed -i 's/\r$//g' /scripts/entrypoint.sh
RUN chmod +x /scripts/entrypoint.sh

COPY ./docker/scripts/install-nginx.sh /scripts/
RUN bash /scripts/install-nginx.sh
COPY ./docker/conf/app.conf /etc/nginx/sites-available/app

RUN rm /etc/nginx/sites-available/default
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled

COPY . /project

ENTRYPOINT ["/scripts/entrypoint.sh"]
