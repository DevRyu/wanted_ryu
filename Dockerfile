FROM python:3.8-slim


RUN apt-get update -y
RUN apt-get install -y build-essential git python3-pip 
RUN pip3 install --upgrade pip 


COPY . /wanted_project
WORKDIR /wanted_project

RUN pip3 install -r requirements.txt
ENV FLASK_APP=wsgi.py


# Listen to port 5000 at runtime
EXPOSE 5000

# Define our command to be run when launching the container
CMD sh run.sh