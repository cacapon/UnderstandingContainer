FROM python:3.6.8-alpine
COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip &&  \
    pip install -r /requirements.txt

WORKDIR /var/private_container
COPY . /var/private_container

ENV FLASK_ENV=development
ENV FLASK_APP=entrance.py

CMD ["python", "entrance.py"]
