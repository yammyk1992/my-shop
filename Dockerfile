FROM python:3.10

ENV PYTHONDONTWRITECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django-shop

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


COPY . .


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
"]

