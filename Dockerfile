FROM python:3.10
EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 manage.py migrate && python3 manage.py collectstatic --noinput && python3 manage.py runserver
