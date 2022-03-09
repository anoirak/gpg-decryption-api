# pull official base image
FROM python:3.9.10-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt update \
    && apt-get install gnupg
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 80

RUN ["chmod" ,"+x" , "./run_tests.sh"]

CMD ["gunicorn" , "--bind", "0.0.0.0:80", "upwork.wsgi:application"]