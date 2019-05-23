FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

ENV LISTEN_PORT=5000
EXPOSE 5000

# Indicate where uwsgi.ini lives
ENV UWSGI_INI uwsgi.ini

# Tell nginx where static files live.
ENV STATIC_URL /acitest/static

# Set the folder where uwsgi looks for the app
WORKDIR /acitest

# Copy the app contents to the image
COPY . /acitest

# If you have additional requirements beyond Flask (which is included in the
# base image), generate a requirements.txt file with pip freeze and uncomment
# the next three lines.



COPY requirements.txt /
RUN pip install  -U pip
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

RUN pip install psycopg2
RUN pip install flask==1.0.3
RUN pip install flask-sqlalchemy==2.3.0
RUN pip install psycopg2==2.7.6.1
#RUN pip install -r /requirements.txt
