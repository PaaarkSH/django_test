# 8. drf 를 활용한 효율적인 웹 API 만들기

# API 서버와 REST

## REST (**Re**presentational **S**tate **T**ransfer)

<aside>
💡 아키텍처 스타일. 프로토콜에 독립적 → 일반적인 REST 구현에서 HTTP를 사용

</aside>

- 순수한 데이터만 필요로 할 때

### Restful API 의 몇가지 디자인 원칙

- 리소스 중심으로 디자인
- 클라이언트에서 엑세스 할 수 있는 모든 종류의 개체 / 서비스가 리소스에 포함
- 리소스마다 해당 리소스를 고유하게 식별하는 식별자 → url 에 1 2 이런걸로 들어가는거
- 요청 응답 포맷으로 json 사용
    - xml → json
    - xml 은 기능은 많지만 json 이 용량이 더 적음
- 균일한 인터페이스 적용
- 리소스 표준 HTTP 동사를 적용
    - GET POST PUT PATCH DELETE

## 리소스를 중심으로 API 구성

- url 작성 방식이 명사 또는 명사 + 식별자
    - 직관적

## 심플하게 URI 구성

- 명사 + 식별자 + 명사 + 식별자 + 명사 → 이런식으로 만들면 유연성이 떨어짐
- 적어도 명사 + 식별자 + 명사 를 마지노선으로 끊어서 개발해야함

## HTTP 메소드를 기준으로

- GET
- POST
- PUT: 기존의 리소스를 대체(리소스를 엎는 개념)
    - 멱등성이 보장됨
- PATCH: 기존의 리소스를 대체
- DELETE
- http 메소드는 더 있지만 restful 에서 이것을 기준으로 개발하긴함

## 요청 응답 형식 지정

- 요청시에 처리를 원하는 형식 지정하면 서버에서 이 형식으로 응답
- 서버에서 해당 형식을 지우너하지 않으면 상태코드 415(지원하지 않는 미디어 유형) 으로 응답

## HTTP Method 별 다양한 상태코드

- 다른건 별로 궁금한 내용은 없음

### 비동기 작업

- 작업 완료시간이 오래 걸릴 경우 다른 Task Queue 프로세서를 만들어 요청을 위임하게 만들어 비동기 처리 가능
    - Celery 등
- 클라이언트가 작업을 Polling 을 통해 모니터링 할 수 있도록 비동기 요청의 상태를 반환하는 URI를 Location header 로 반환
    - Polling: 주기적으로 대상을 검사
    - 뭐 이렇게는 안써봤는디

## 보통의 API 는 HTTP API 라고 불러야 하지 않는가?

- rest api 라고 부르는 것들은 단순히 http 프로토콜을 통한 api 라 web api 또는 http api 라고 부르는게 맞음
- 대부분의 Rest API 들은 Rest 아키텍처 스타일 X

## Django rest framework

### 설계역역에 대해서는 다루지 않음

- 장고의 패러다임 하에 빠르고 관리하기 쉬운 API

### 이것이 REST api 의 전부는 아님

- uri 는 ‘https://{serviceRoot} / {collection} / {id}’ 형식 이어야 함
- GET PUT DELETE POST HEAD PATCH OPTIONS 를 지원해야함
- API 버저닝은 major, minor 로 하고 uri 에 버전 정보를 포함해야함

## drf 의 주요 기능들

- **Serializer / ModelSerializer 를 통한 데이터 유효성 검증 및 데이터 직렬화**
    - form 과 유사
- 각종 Parser 를 통한 데이터 처리
    - 요청 포맷이 다양할 수 있는데 일관되게 처리
        - application json 으로 반환
- APIView Generic ViewSet ModelViewSets 를 통한 요청 처리
- 각종 Renderer 를 통한 다양한 응답 포맷 지원
- 인증 / 권한 체계
    - drf 기본에서는 토큰 인증만 지원해주게 되어있음
    - 서드파티를 통해 JWT 지원
- Throttling: 최대호출 횟수 제한
    - 일반 유저는 100회 프리미엄은 1000회 이런거

## CRUD

### 모든 데이터는 기본적으로 ‘추가 조회 수정 삭제’ 액션으로 관리될 수 있음

- C: Create 생성
    - 새 레코드 생성
- R: Read, Retrieve 조회
    - 레코드 목록 조회, 특정 레코드 조회
- U: Update 수정
    - 특정 레코드 수정
- D: Delete 삭제
    - 특정 레코드 삭제

<aside>
💡 주의! CRUD 는 리소스에 대한 대표적인 동작일 뿐 API 전부는 아님

</aside>

# JSON 응답뷰 만들기