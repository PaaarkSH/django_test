FROM postgres:13

# 개인 로컬 설치용 dockerfile
# 환경변수 설정
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_DB=mypostgres
ENV POSTGRES_USER=service_user

# 포트 설정
EXPOSE 5432

# 컨테이너 시작 시 PostgreSQL 실행
CMD ["postgres"]