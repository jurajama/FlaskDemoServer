FROM python:3.8-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ["requirements.txt", "./"]
RUN pip install -r requirements.txt

# Bring source code into image
COPY src/ .

# Use gunicorn to server flask app, not flask's dev/test server
EXPOSE 5090
CMD ["gunicorn", "--chdir", "/app", "--bind", "0.0.0.0:5090", "--workers", "3", "application:create_app('config')"]
