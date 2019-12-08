#Pull down the necessary image
FROM python:3
#create app folder 
COPY ./nginx/uwsgi_flask_rest.service /etc/systemd/system/
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /usr/src/app
#change working directory
WORKDIR /usr/src/app
#copy requirements.txt and install dependecies
COPY requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt
#copy the souce code to app dir
COPY . /usr/src/app
#expose port in which app will run
EXPOSE 5001
# Process to run when image is used to crate a container
ENTRYPOINT ["python"]
CMD ["app.py"]
