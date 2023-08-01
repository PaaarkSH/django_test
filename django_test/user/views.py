from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test, permission_required
from rest_framework.decorators import api_view
from library.decorator import custom_login_required  # 로그인 여부 체크후 로그인 안되어있으면


@custom_login_required
@transaction.atomic
def user_view(request):
    pass

