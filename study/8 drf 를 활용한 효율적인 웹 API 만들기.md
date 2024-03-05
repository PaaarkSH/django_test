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

- 딱히 대단한건 없던데
    - 내가 원하는 drf 는 아니였음
- postman 말고 HTTPie 설명해주는건 살짝 킹받음
- 이제 드디어 ModelViewSet 사용함
    - `def dispatch()`
        - ModelViewSet 안에 들어가있는데 그냥 재정의 하지 말고 dispatch 를 실행하는 단계에서

# APIView 를 활용한 뷰 만들기

## APIView

- 하나의 cbv → 하나의 url 만 처리 가능
    - 이것을 통함한것이 `generic` → `viewset`
    - 정확히는 `APIView` → `mixins` → `generics` → `viewset`
- 클래스 기반의 `APIView` 가 있고 함수기반의 데코레이터 `@api_view` 가 있음
- 각 method 에 맞게 함수를 구현하면 호출 가능
- `distpatch` 함수는 APIView 내부에 있었음

## `@api_view`

- 하나의 구현만 할때 편리함

# Mixins 상속을 통한 APIView

- 다른 클래스에 의해서 상속이 이루어질때 사용

## generic APIView 함수 종류

### get

- retireve: 단일 객체
- list: 리스트

### post

- create

### put

- update

### patch

- partial_update

### delete

- destroy

## 중복 줄이기 가능

# ViewSet과 Router

## 단일 리소스에서 관련있는 View들을 단일 클래스에서 제공

- model viewset 에 기본적인 구현이 다 되어있음
- router 함수를 통해 해당 함수 디스패치

## ModelViewSet

### 2가지 ModelViewSet

### ReadOnlyModelViewSet

- get 요청에만 반응
- list 지원
- detail 지원

### ModelViewSet

- 전체 다 지원
- list create 지원
- detail / update / partial_update / delete 지원

## @action

- model viewset 에 커스텀한 기능을 넣을때 사용

# Form 과 Serializer 관점에서 drf 비교

## 커스텀 유효성 검사 루틴 - clean_ vs validate_

- clean_
    - form 에서 is_valid 함수 호출시 사용
- validate_
    - 시리얼라이저의 is_valid 함수에서 호출
    - 시리얼라이저 코드에서 정의

# 유효성 검사

## is_valid 호출 되고 난 이후

- initial_data 필드에 접근
- validated_Data 를 통해 유효성 검증에 통과한 값들이 .save() 함수에 사용
- .errors: 유효성 검증 수행 후에 오류 내영
- .data: 유효성 검증 후에, 갱신된 인스턴스에 대한 필드값 딕셔너리

## Serializer 는 form 과 사용법이 유사하지만 생성자에 차이가 있음

- 생성자 안에 data 변수를 통해 validate 수행

## DRF 에서는 유효성 체크를 도와주는 Validators 제공

- 많아서 다 적지는 않겠음

## perform 계열 함수

- APIView의 create update destroy 맴버 함수에서 실질적인 db 처리 로직은 perform_create 와 같은 perform 계열 함수에서 이루어짐
- 실제 동작을 수행하는 부분들
- 이유는 보자면 create 함수의 원형을 봐도 create 함수 안에서 perform_create 함수의 기능을 동작함

## Create 시에 추가로 저장할 필드가 있다면?

### 모델에 ip 필드가 있고 유저의 아이피를 저장하고 싶다면?

- `def perform_create(self, serializer):
         serializer.save(ip=self.request.META[’REMOTE_ADDR’])`
    - 기존의 모델에서 ip 를 추가하고 save 함수에서 ip 파라미터를 ip 값을 직접 변수로 할당해서 넘겨줘버리면 됨
    - 강사님은 author 가 필수키셔서 author 도 같이 넘겨주셔야됬음

# Authentication 과 Permission

## 인증

- 유입되는 요청을 허용 거부 하는것을 결정하는것이 아닌
단순히 인증 정보로 유저를 식별
- Authentication: 유저 식별
- Permissions: 각 요청에 대한 허용 거부
- Throtting: 일정 기간동안 허용할 최대 요청 횟수

## DRF 의 permission

- view 단위에서 permission 을 설정할 수 있음

### cbv

- `permission_classes = [IsAuthenticated]`

### fbv

- `@permission_classes([IsAuthenticated])`

## 디폴트 전역 설정

```python
REST_FRAMEWORK = {
   ‘DEFAULT_PERMISSION_CLASSES’ : [
         ‘rest_framework.permissions.IsAuthenticated’    # default 가 allowany
	 ]
}
```

- settings 단계에서 설정해줘야함
- 

# Token 인증

## DRF 가 지원하는 인증

- session: 웹 프론트 엔드랑 같은 호스트를 사용하면 세션 인증 가능
    - 외부 서비스는 불가능
- BasicAuthentication: 매번 username / password 를 넘겨서 인증
    - 보안상 위험한짓

### TokenAuthentication

- 초기에 username password 로 Token 을 발급받아 해당 토큰을 매번 api 요청을 통해 담아 보내서 인증 처리

## Token 모델

- drf 라이브러리 안에 authtoken 이라는 별도의 app 이 있고 안에 모델이랑 모든게 구현되어있음
- 각 User 모델과 1:1 관계
- 각 User 별 Token 은 수동으로 생성
- Token 은 User 별로 유일하며 Token 만으로 인증을 수행

## 토큰을 생성하기 위한 3가지 방법

### ObtainAuthToken 뷰를 통한 생성

- urlpattern 에 등록해서 만들면됨
- post 를 통한 생성시에 token 을 리스폰스에 넣어서 반환 가능

### Signal 을 통한 자동 생성

```python
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
```

- post_save
    - signals 라이브러리의 함수
    - save 가 이루어진 이후에 발생되는 일종의 콜백
- AUTH_USER_MODEL 유저 모델을 지정해서 유저 모델이 save 될 때 호출됨
- created 라는 파라미터를 받을 수 있는데 해당 파라미터가 참일 경우만 토큰 생성

### Management 명령을 통한 생성

- 이거는 매우 좋은 방법은 아닐듯

# JWT 인증

## 토큰 인증과 JWT 인증

- jwt: json web token
- 일반적인 토큰이나 jwt 나 토큰의 역활인건 같음

## DRF 의 Token

- 다순 문자열
    - user 와 1:1 매칭
    - 유효기간 없음
- 토큰은 해시화해서 db 에 넣어놨으니 역순으로 찾아야함

## JWT

- db 를 조회하지 않아도 로직으로 인증 가능
- 포맷: 헤더 내용 서명
    - 서버에서 토큰 발급시 비밀 키로 서명하고 발급 시간을 저장
    - 서명은 함호화가 아님
        - 누구라도 열어볼수있기에 보안성 데이터가 아니라 필요한 정보만
- claim: 담는 정보의 한 조각, key value 형식
- 위변조 불가
    - 장고에서는 settings.SECRET_KEY 를 사용하거나 JWT_SECRET_KEY 설정
    - 장고에서 프로젝트 생성되면 기본으로 나옴
- 갱신(refresh) 매컨니즘을 사용
    - 유효기간 내에 갱신하거나 id / pw 를 통해 재인증
- 이미 발급된 토큰을 폐기하는 것은 불가능함

## 토큰과 jwt

- 기존의 토큰 보다 jwt 의 토큰의 길이가 매우 김
- jwt 구조
    - header
        - base64 인코딩
        - 어떤 타입인지 무슨 알고리즘을 썼는지 이런 정보
    - payload
        - base64 인코딩
        - user_id 나 username 이런거
            - 읽을수있지만 payload 를 변조하게되면 서명이 변경됨
    - signture(서명)
        - header payload 를 조합하고 비밀키로 서명한 이후에 인코딩함
        - 이 signture 덕분에 변조가 불가능함

## JWT의 Life Cycle

- 만료 시간이 있고 Refresh 를 지원함

## 안전한 장소에 보관

- 일반 토큰 jwt 토큰 여부에 상관없음
- 스마트폰 앱은 설치된 앱 별로 안전한 저장 공간이 제공되지만 웹 브라이주어에는 없음
- 토큰은 앱 환경에서만 권장함
- 웹 환경에서는 session 인증이 나은 선택일 수 있음
    - 장고의 세션은 웹 클라이언트가 같은 host 여야함

## djagnorestframework-jwt

```python
REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES' : [
		...
	],
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
	]
}

JWT_AUTH = {
	'JWT_ALLOW_REFRESH': True,
}
```

- settings 파일에 추가해줘야함

```python

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
urlpatterns = [
	path('api-jwt-auth/$', obtain_jwt_token),
	path('api-jwt-auth/refresh/$', refresh_jwt_token),
	path('api-jwt-auth/verify/$', verify_jwt_token),
]
```

- urlpatterns 구현
- username 과 password 를 통한 응답을 통해서 발급받을 수 있음
    - 파라미터를 username password 로 넘기면 됨
- 이제 JWT 토큰을 매 요청시마다 header 에 Authorization 값으로 넘겨주면 됨

## 유효기간이 지났다면?

- 유효 기간 내에 갱신해야함
- 유효기간은 settings 의 JWT_EXPIRATION_DELTA 에서 시간 변경해줘야함

## 갱신

- settings.JWT_AUTH 의 JWT_ALLOW_REFRESH 의 설정을 True 로 해놓을 경우만 갱신 지원
    - 디폴트는 False