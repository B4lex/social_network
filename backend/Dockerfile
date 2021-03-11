FROM python:3.8

WORKDIR /code
COPY . .
RUN chmod +x ./docker-entrypoint.sh
RUN python3 -m pip install -r requirements.txt
WORKDIR src
EXPOSE 8000
