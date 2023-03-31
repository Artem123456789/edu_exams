FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get install -y nginx
RUN apt-get install -y build-essential
RUN apt-get install -y libpq-dev
RUN apt-get install -y gettext
RUN apt-get -y install libev-dev
RUN apt-get -y install gcc
RUN apt-get install -y htop
RUN apt-get install -y git

WORKDIR /project

COPY ./requirements.txt requirements.txt
RUN pip install --default-timeout=1000 -r /project/requirements.txt

COPY ./docker/scripts/run_django /scripts/run_django
RUN sed -i 's/\r$//g' /scripts/run_django
RUN chmod +x /scripts/run_django

COPY ./docker/scripts/entrypoint /scripts/entrypoint
RUN sed -i 's/\r$//g' /scripts/entrypoint
RUN chmod +x /scripts/entrypoint

COPY ./docker/scripts/entrypoint /scripts/entrypoint
RUN sed -i 's/\r$//g' /scripts/entrypoint
RUN chmod +x /scripts/entrypoint

COPY ./docker/scripts/install-nginx.sh /scripts/
RUN bash /scripts/install-nginx.sh
COPY ./docker/conf/app.conf /etc/nginx/sites-available/app

RUN rm /etc/nginx/sites-available/default
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled

COPY . /project

ENTRYPOINT ["/scripts/entrypoint"]
