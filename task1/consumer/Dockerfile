FROM python:3.6-alpine
WORKDIR /code
ADD requirements.txt /code/requirements.txt
ADD consumer.py /code/consumer.py
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev &&\
    pip install -r requirements.txt

CMD ["python", "/code/consumer.py"]
