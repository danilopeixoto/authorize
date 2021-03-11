FROM python:3.6

LABEL description "Authorizer for bank transactions."
LABEL version "1.0.0"
LABEL maintainer "Author <author@stone.com.br>"

WORKDIR /usr/src/authorize/
COPY . .

RUN pip install --upgrade pip
RUN pip install .

ENTRYPOINT ["authorize"]
