FROM python:3.8-slim-buster

COPY requirements.txt /tmp
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt

WORKDIR /usr/src/app
COPY . .

CMD ["gunicorn", "edu_exams.wsgi:application", "--bind", "0.0.0.0:8000"]
