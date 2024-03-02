# 장고 테스트용 프로젝트

## 장고 기술 테스트 목적 프로젝트

docker image ls
docker rmi payhere
docker build -t payhere -f Dockerfile .
docker run -p 8000:8000 payhere gunicorn base.wsgi:application --bind 0.0.0.0:8000
docker run -d --rm --name payhere -p 8000:8000 payhere gunicorn base.wsgi:application --bind 0.0.0.0:8000
    docker run: 도커 컨테이너를 실행하는 명령어입니다.
    -d: 컨테이너를 데몬(Daemon) 모드로 실행합니다. 즉, 백그라운드에서 실행됩니다.
    --rm: 컨테이너가 종료되면 컨테이너를 자동으로 삭제합니다. 이 옵션을 사용하면 컨테이너를 실행하고 종료했을 때 임시 컨테이너 파일이 남지 않습니다.
    --name payhere: 컨테이너의 이름을 payhere로 지정합니다.
    -p 8000:8000: 호스트의 8000 포트를 컨테이너의 8000 포트와 매핑합니다. 즉, 호스트의 8000 포트로 접속하면 컨테이너의 8000 포트로 연결됩니다.
    payhere: 실행할 도커 이미지의 이름입니다.
    gunicorn base.wsgi:application --bind 0.0.0.0:8000: 컨테이너 안에서 실행할 명령어입니다. 
    gunicorn은 Python의 WSGI HTTP Server로, Django 애플리케이션을 실행하는 데 사용됩니다. 
    base.wsgi:application은 Gunicorn이 실행할 Django 애플리케이션의 엔트리 포인트를 지정합니다.
     --bind 0.0.0.0:8000은 Gunicorn이 0.0.0.0 IP 주소와 8000 포트에서 요청을 기다리도록 지정합니다.
        

## 추가사항