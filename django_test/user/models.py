from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, password, name, **extra_fields):
        if not user_id:
            raise ValueError("아이디가 설정 안되었습니다")
        if not password:
            raise ValueError("비밀번호가 설정 안되었습니다")
        if not name:
            raise ValueError("사용자 이름이 설정 안되었습니다")
        user = self.model(user_id=user_id, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자에 대한 기능은 사용은 안할 계획입니다
    def create_superuser(self, user_id, password=None, name=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(user_id, password, name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    사용자 아이디
    이름
    활성화 여부
    """

    user_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    objects = CustomUserManager()
    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        db_table = "myuser"

    def __str__(self):
        return self.user_id
