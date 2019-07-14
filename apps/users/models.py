from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女"),
)


class UserProfile(AbstractUser):
    # 昵称刚注册的时候可以为空 使用null blank 或者使用default=""
    nick_name = models.CharField(verbose_name="昵称", max_length=50, default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", max_length=6, choices=GENDER_CHOICES)
    address = models.CharField(verbose_name="地址", max_length=120, default="")
    mobile = models.CharField(verbose_name="手机号码", max_length=11, unique=True)
    image = models.ImageField(verbose_name="头像", upload_to="head_image/%Y/%m", default='default.jpg', max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        return self.username


class BaseModel(models.Model):
    create_time = models.DateField(verbose_name="创建时间", default=datetime.now)

    class Meta:
        abstract = True
