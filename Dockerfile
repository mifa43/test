FROM python:3.8

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

ENV DJANGO_EMAIL_PASSWORD ${DJANGO_EMAIL_PASSWORD}

COPY . /code/

CMD ["/bin/bash", "server.sh"]