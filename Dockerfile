FROM python:3-alpine3.14
LABEL authors="marton.aron"

COPY backend app
# .env file needs to be created
COPY requirements.txt app

ENTRYPOINT ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python", "api.py"]

EXPOSE 5000