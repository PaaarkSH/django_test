from rest_framework.response import Response


def custom_login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # 로그인되지 않았을 때 원하는 처리를 수행합니다.
            message = "로그인이 필요한 페이지입니다."
            return Response(data=message, status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
