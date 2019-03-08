FROM python:3.6-alpine
COPY requirements.txt /code/requirements.txt
COPY manage.py /code/manage.py
COPY run_service.sh /code/run_service.sh
WORKDIR /code
RUN apk add --no-cache postgresql-libs gcc musl-dev postgresql-dev 
RUN pip install -r requirements.txt

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "run_service.sh"]
