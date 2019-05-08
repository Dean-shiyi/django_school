from django.db import models

# Create your models here.


class SchoolEvents(models.Model):
    title = models.CharField(max_length=100, verbose_name='事件标题')
    time = models.TimeField(verbose_name='事件时间段')
    date = models.DateField(verbose_name='事件日期')
    addr = models.CharField(max_length=100, verbose_name='事件发生地点')
    desc = models.CharField(max_length=255, verbose_name='事件描述')
    img = models.ImageField(upload_to='event_pic', null=True, default=None, blank=True)

    class Meta:
        db_table = 'SchoolEvent'

    def __str__(self):
        return self.title


class ClientsSay(models.Model):
    name = models.CharField(max_length=100, verbose_name='学员名字')
    lesson = models.CharField(max_length=20, verbose_name='所学专业')
    words = models.CharField(max_length=255, verbose_name='学员感言')
    img = models.ImageField(upload_to='client_pic', null=True, default=None, blank=True)

    class Meta:
        db_table = 'ClientSay'

    def __str__(self):
        return self.name


