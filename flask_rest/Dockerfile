FROM tiangolo/uwsgi-nginx-flask:python3.7
ENV LISTEN_PORT 5002
#ENV STATIC_INDEX 1
ENV UWSGI_INI /app/uwsgi.ini
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5002
COPY ./app /app
COPY ./tests /tests
