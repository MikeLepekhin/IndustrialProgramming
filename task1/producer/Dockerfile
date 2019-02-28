FROM python:3.6-alpine
WORKDIR /code
ADD requirements.txt /code/requirements.txt
ADD producer.py /code/producer.py
RUN pip install -r requirements.txt

CMD ["python", "/code/producer.py"]
