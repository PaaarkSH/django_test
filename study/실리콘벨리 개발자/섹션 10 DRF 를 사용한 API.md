# 섹션 10 DRF 를 사용한 API

# API 란 무엇인가

- 위키피디아: 두 개 이상의 컴퓨터 프로그램이 커뮤니케이션을 위해 사용
- 기존에 open api 중에는 swagger 가 가장 인기가 많지만
- 요즘 **drf-spectacular** 가 가장 활발하다 하심
    - 장고 4.1 도 지원
- OpenAPI Schema: api 개발 스탠다드
    - swagger 회사에서 만들었다고 했음

```python
INSTALLED_APPS = [
    ...
    'drf_spectacular',
    ...
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Django Test",
    "DESCRIPTION": "For Django Test",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
```

- DEFAULT_SCHEMA_CLASS
    - 프로그래머가 직접 코드를 작성하지 않고 API 문서를 생성
    - drf 시리얼라이저, 뷰 및 쿼리 파리미터를 기반으로 시키마 생성
- SERVE_INCLUDE_SCHEMA
    - 스키마 문서를 api 응답에 포함할지 여부
    - 디폴트가 False

# 직렬화

## Serializers

- 쿼리셋이나 모델 인스턴스 같은 것을 파이썬 데이터 타입으로 변경
    - json , xml
- 반대로 json 타입의 데이터를 모델 인스턴스로 변경가능
- 장고의 form 과 비슷
- ModelSerializer 가 있음
    - 기존의 model form 은 Meta 에 연결해서 쉽게 사용했었음
    - 시리얼라이저도 같음

## 시리얼라이저 프로세스

- 모델 인스턴스 → 번역 → 파이썬 데이터 타입 → 렌더 → json
- json → 역직렬화 → 파이썬 데이터 타입 → 번역 → 모델 인스턴스
- 

# Request and Response

## drf 의 Request and Response

- drf 는 http request response 와 template  request response 제공
- 원래 미들웨어 때문에 request response 를 변경 할 수 없지만 template 이 지연로딩으로 값을 변경하도록 도움
- 상태코드 제공
- api view 를 제공하기 위한 Wrapper 를 제공
    - `@api_view`
        - decorator
    - `APIView`
        - class

# CBV

## CBV `APIView`

- http 메소드를 중심으로 나눠짐
- decorator 없이 mixin 을 사용한 기능 추가
- 기존의 generic 이나 기능별 함수 뷰 들을 합쳐놓음
- 그냥 APIView 를 통한 api 생성 가능
- get post 에 대한 기능을 정의하고 사용
    - 내가 알기로는 정의 안해도 될텐데

## DRF Mixins + Generic APIView

- mixins + generic 상속 하는 방법도 있음
    - 기존의 APIView 는 APIView 만 상속받음
- 쿼리셋이랑 시리얼라이저 클래스를 지정해놓고 연결해서 사용

## DRF Generic CBV

- generic 에서 지원하는 List + Create 가 합쳐진 view 를 사용한다던가
- 결국 mixin 이 코드 내에서 선언을 하지 않음

## 코드 간결화 과정

- 장고 fbv → drf fbv → drf APIView → DRF Mixins + Generic APIView → drf generic CBV
- 오른쪽으로 갈수록 코드가 심플해지고 왼쪽으로 갈수록 코드가 더 수정 가능해지는걸 볼 수 있음

# 인증과 허가

## 인증과 허가

- 인증: 신원을 확인하는 절차
- 허가: 인증된 회원이 가질 수 있는 권한

## 사용법

- generic 클래스 선언시 permissioon 지정 가능
    - `permission_classes = [permissions.IsAuthenticatedOrReadOnly]`

# Viewsets 와 Routers

## 뷰셋과 라우터

- 모델에 대해 특화됨
- viewset 사용시 list create retrieve update detroy 를 한번에 구현되어있는걸 사용하면됨
- @action 데코레이터가 추가됨
    - 이거는 사실 렌더용
- 이제 urlpatterns 에서 router 함수를 설정하고 viewset 을 연결하면 사용 가능

# APIView 와 Viewset 의 차이점

## APIView

- http 메소드 중심 함수
- **model 에 있어서 CRUD 가 필요 없는 API 에 사용**
    - CRUD 가 필요한 부분에 있어서는 Viewset 을 사용해야함
- 그래서 커스텀 로직을 사용하는데 좋음
- CBV FBV 둘다 사용
- 난 그래서 로그인 하는 기능에다가 사용했었음

## Viewset

- generic 클래스의 여러 view 들을 한꺼번에 사용하기 좋도록 사용
- model 에 대한 CRUD 를 사용하기 좋게 만들어놨음
- 다른 프레임워크에서는 Resource 또는 Controller 라고 부름
- 장고 모델에 대해서 사용
- routers 를 통해 url 을 사용