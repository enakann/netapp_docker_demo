FROM tiangolo/uwsgi-nginx-flask:python3.7
ENV LISTEN_PORT 5001
#ENV STATIC_INDEX 1
ENV UWSGI_INI /app/uwsgi.ini
EXPOSE 5001
COPY ./app /app

