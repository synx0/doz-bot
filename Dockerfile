FROM python:3.8-buster

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python3 ./main.py