FROM python:3.9

WORKDIR /opt/app

COPY . .

EXPOSE 8000

CMD [ "python", "app.py" ]
