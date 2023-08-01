#!/bin/bash

# Gunicorn 서버 실행
gunicorn base.wsgi:application --bind 0.0.0.0:8000
#!/bin/bash