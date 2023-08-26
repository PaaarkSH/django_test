FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=base.settings.base

WORKDIR /
COPY . /

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /entrypoint.sh
RUN chmod +x /wait-for-it.sh

# Gunicorn 실행
CMD ["./entrypoint.sh"]
