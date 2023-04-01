#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

NGINX_MAX_UPLOAD=0
NGINX_WORKER_PROCESSES=1
service nginx start

nginx_ready() {
    code=$(curl -s -o /dev/null -w "%{http_code}" 'localhost:80')
    if [[ $code != 000 ]];
    then
        return $(true)
    else
        nginx -c /etc/nginx/nginx.conf -g 'daemon on;'
        return $(false)
    fi
}

until nginx_ready; do
  >&2 echo 'Waiting for NGINX to become available...'
  sleep 1
done
>&2 echo 'NGINX is available'

python manage.py migrate
python manage.py collectstatic --no-input

# gunicorn start
# -----------------------------------------------------------------------------
GUNICORN_MAX_WORKERS=3

if [ -z ${GUNICORN_WORKERS+x} ];
then
	GUNICORN_WORKERS=1
else
    if (( $GUNICORN_WORKERS > $GUNICORN_MAX_WORKERS ));
    then
        GUNICORN_WORKERS=$GUNICORN_MAX_WORKERS
    fi
fi

if [ -z ${GUNICORN_TIMEOUT+x} ];
then
	GUNICORN_TIMEOUT=60
fi

if [ "$DJANGO_SETTINGS_MODULE" = "config.settings.settings" ];
then
    gunicorn config.wsgi:application \
        --workers $GUNICORN_WORKERS \
        --timeout $GUNICORN_TIMEOUT \
        --keep-alive 5 \
        --bind 0.0.0.0:8000 \
        --chdir=/project \
        --log-level=info \
        --log-file=-
else
    gunicorn config.wsgi:application \
        --reload \
        --workers $GUNICORN_WORKERS \
        --timeout $GUNICORN_TIMEOUT \
        --keep-alive 5 \
        --bind 0.0.0.0:8000 \
        --chdir=/project \
        --log-level=debug \
        --log-file=-
fi