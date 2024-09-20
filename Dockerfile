FROM python:3.11-alpine as package
RUN apk add --no-cache gcc musl-dev libffi-dev
RUN apk add --no-cache bash
ENV SERVICE_DIR=/app
RUN mkdir -p $SERVICE_DIR
WORKDIR $SERVICE_DIR

RUN pip install --upgrade pip

ADD requirements.txt $SERVICE_DIR/requirements.txt
RUN pip install -r requirements.txt

FROM package

ENV PYTHONUNBUFFERED=1

ADD courses $SERVICE_DIR/courses
ADD educa $SERVICE_DIR/educa
ADD students $SERVICE_DIR/students

ADD favicon.ico $SERVICE_DIR/favicon.ico
ADD Procfile $SERVICE_DIR/Procfile

ADD manage.py $SERVICE_DIR/manage.py
ADD initadmin.py $SERVICE_DIR/initadmin.py

RUN python manage.py migrate
RUN python manage.py initadmin

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]