from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from library.lib import get_request_data


class UserViewSet(viewsets.ModelViewSet):
    """
    user 모델의 crud 관리를 위한 뷰셋 클래스
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        """
        유저 삭제 api
        - 유저 삭제 테스트를 위해 추가했습니다
        """
        user_id = kwargs.get("pk")  # URL에서 user_id를 가져옴
        try:
            user = User.objects.get(user_id=user_id)  # user_id로 회원을 찾음
            user.delete()  # 회원 삭제
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def logout(request):
    """
    로그아웃 기능 구현
    - orm 과 관련 없는 기능은 fbv 로 구현했습니다
    """
    response = Response(data={"message": "로그아웃되었습니다."}, status=status.HTTP_200_OK)
    response.set_cookie("access_token", "", expires=0)
    response.set_cookie("refresh_token", "", expires=0)
    return response
