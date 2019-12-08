#Pull down the necessary image
FROM python:3-alpine
#create app folder 
RUN mkdir -p /usr/src/app
#change working directory
WORKDIR /usr/src/app
#copy requirements.txt and install dependecies
COPY requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt
#copy the souce code to app dir
COPY . /usr/src/app
#expose port in which app will run
EXPOSE 5000
# Process to run when image is used to crate a container
CMD ["python app.py"]
