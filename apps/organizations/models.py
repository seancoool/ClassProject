from django.db import models
from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(verbose_name="城市名称", max_length=20)
    description = models.CharField(verbose_name="描述", max_length=200)

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name


class Organization(BaseModel):
    name = models.CharField(verbose_name="机构名称", max_length=50)
    description = models.TextField(verbose_name="描述")
    tag = models.CharField(verbose_name="机构标签", max_length=10, default='全国知名')
    category = models.CharField(verbose_name="类别", max_length=4, default='pxjg',
                                choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')])
    fav_num = models.IntegerField(verbose_name="收藏数)", default=0)
    click_num = models.IntegerField(verbose_name="点击次数)", default=0)
    stu_num = models.IntegerField(verbose_name="学习人数)", default=0)
    course_num = models.IntegerField(verbose_name="课程数)", default=0)
    address = models.CharField(verbose_name="机构地址", max_length=150)
    logo = models.ImageField(verbose_name="logo", upload_to="org/%Y/%m", max_length=100)
    city = models.ForeignKey(City, verbose_name="所在城市", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name


class Teacher(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(verbose_name="姓名", max_length=50)
    age = models.IntegerField(verbose_name="年龄)", default=18)
    work_year = models.IntegerField(verbose_name="工作年限)", default=0)
    work_company = models.CharField(verbose_name="就职公司", max_length=50)
    work_position = models.CharField(verbose_name="公司职位", max_length=50)
    fav_num = models.IntegerField(verbose_name="收藏数)", default=0)
    click_num = models.IntegerField(verbose_name="点击次数)", default=0)
    image = models.ImageField(verbose_name="头像", upload_to="teacher/%Y/%m", max_length=100)

    class Meta:
        verbose_name = "讲师"
        verbose_name_plural = verbose_name

