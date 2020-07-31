FROM python:3.6.8-alpine
COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip &&  \
    pip install -r /requirements.txt

WORKDIR /var/pubric_container
COPY . /var/pubric_container

ENV FLASK_ENV=development
ENV FLASK_APP=entrance.py

CMD ["python", "entrance.py"]
