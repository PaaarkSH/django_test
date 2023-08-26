#!/bin/bash

# db 사용 가능까지 기리는 스크립트 코드
echo "db 사용을 기다리는 중입니다"
./wait-for-it.sh db:5432 -t 120

WAIT_FOR_IT_RESULT=$?
if [[ $WAIT_FOR_IT_RESULT -eq 0 ]]; then
    echo "db 사용이 가능합니다"
    python manage.py makemigrations
    python manage.py migrate
    gunicorn base.wsgi:application --bind 0.0.0.0:8000
else
    echo "db 사용 대기 중에 문제가 발생하였습니다."
fi