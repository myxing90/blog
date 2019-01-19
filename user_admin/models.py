# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.urls import reverse
from DjangoUeditor.models import UEditorField


# 注册用户---------------------------------------------------------------
class Reg_user(models.base.Model):
    username = models.fields.CharField('用户名', max_length=20, unique=True)
    password = models.CharField('密码', max_length=120)
    email = models.EmailField('邮箱', blank=True)
    reg_time = models.DateTimeField('注册时间', auto_now_add=True)
    # last_login = models.DateTimeField()

    #以下为可选字段，用户可在后台自己设置
    user_img = models.FileField(
        '用户图片', upload_to='author_img', default='author_img/user_normal.jpg')
    mobile_num = models.IntegerField('手机号码', blank=True, null=True)
    sex = models.CharField('性别', max_length=2, blank=True)
    birthday = models.DateField('生日', blank=True, default='2000-1-1')
    self_intro = models.CharField('自我介绍', max_length=100, blank=True)
    my_tag = models.CharField('我的标签', max_length=10, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'A1_注册用户'
        ordering = ['-reg_time']

    def get_img_url(self):
        if self.user_img:
            return self.user_img.url
        else:
            return '/upload/author_img/user_normal.jpg'

    def get_author_url(self):
        return reverse('tag', args=(self.username, ))


class Reg_user_admin(admin.ModelAdmin):
    list_display = ('username', 'email', 'reg_time', 'user_img')


admin.site.register(Reg_user, Reg_user_admin)
