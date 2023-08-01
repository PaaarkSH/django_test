FROM python:3.11.4

ENV DJANGO_SETTINGS_MODULE=base.settings.base

WORKDIR /django_test
COPY . /django_test/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations orm_test
RUN python manage.py migrate orm_test

EXPOSE 8000

COPY entrypoint.sh /django_test/entrypoint.sh
RUN chmod +x /django_test/entrypoint.sh

CMD ["./entrypoint.sh"]
