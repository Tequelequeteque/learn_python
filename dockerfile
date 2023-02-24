FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install pipenv

CMD pipenv install && pipenv run debug