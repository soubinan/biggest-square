FROM python:3.9


COPY . /opt/app
WORKDIR /opt/app

EXPOSE 8080

CMD [ "python", "app.py" ]