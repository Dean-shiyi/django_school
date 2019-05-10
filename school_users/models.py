from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUsers(AbstractUser):
    def __str__(self):
        return self.username


class AdmissionInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name='学生姓名', blank=True)
    birth = models.CharField(max_length=100, verbose_name='学生生日', blank=True, )
    gender = models.CharField(max_length=10, verbose_name='学生性别', blank=True)
    Email = models.EmailField(max_length=254, verbose_name='学生邮箱', blank=True)
    Phone = models.CharField(max_length=11, verbose_name='学生电话', blank=True)
    course = models.CharField(max_length=50, verbose_name='选择课程', blank=True)
    course_time = models.CharField(max_length=50, verbose_name='课程时间', blank=True)
    addr = models.CharField(max_length=255, verbose_name='学生地址', blank=True)
    line = models.CharField(max_length=255, verbose_name='xxx', blank=True)
    city = models.CharField(max_length=50, verbose_name='城市', blank=True)
    zip_code = models.CharField(max_length=20, verbose_name='邮编', blank=True,default="")

    class Meta:
        db_table = 'AdmissionInfo'

    def __str__(self):
        return self.name
