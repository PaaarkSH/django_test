from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test, permission_required
from rest_framework.decorators import api_view


@login_required  # 로그인 여부를 체크하여, 로그아웃 상황에서는 로그인 페이지로 이동 시키고 로그인 상황에서만 해당 뷰를 호출
@transaction.atomic
def user_view(request):
    pass

