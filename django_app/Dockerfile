FROM python:3.11

WORKDIR /opt/app

ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt \
     && pip install gunicorn \
     && mkdir -p /opt/app/static

COPY . .

RUN chmod +x /opt/app/django_entrypoint.sh

ENTRYPOINT ["sh", "/opt/app/django_entrypoint.sh"]