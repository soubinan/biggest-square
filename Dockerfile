FROM python:3.9

WORKDIR /opt/app

COPY . .

EXPOSE 8080

CMD [ "python", "app.py" ]
