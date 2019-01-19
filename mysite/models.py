# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.urls import reverse
from DjangoUeditor.models import UEditorField
from user_admin.models import Reg_user
import re


# 热门网址-------------------------------------------------------------------
class Top_url(models.Model):
    name = models.CharField('名称', max_length=15)
    url = models.URLField('网址')
    logo = models.FileField('LOGO', upload_to='url_logo')
    rank = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'B1_热门网址'
        ordering = ['rank']


class Top_url_admin(admin.ModelAdmin):
    list_display = ('name', 'url', 'logo', 'rank')


admin.site.register(Top_url, Top_url_admin)


# 分类网址标签、分类网址-----------------------------------------------------
class Sort_tag(models.Model):
    name = models.CharField(max_length=10)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'B2_分类标签'
        ordering = ['rank']


class Sort_url(models.Model):
    sort = models.ForeignKey(Sort_tag,on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    url = models.URLField()
    logo = models.FileField(upload_to='url_logo', blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'B3_分类网址'
        ordering = ['sort', 'rank']


class Sort_tag_admin(admin.ModelAdmin):
    list_display = ('name', 'rank')


admin.site.register(Sort_tag, Sort_tag_admin)


class Sort_url_admin(admin.ModelAdmin):
    list_display = ('sort', 'name', 'url', 'logo', 'rank')


admin.site.register(Sort_url, Sort_url_admin)


# 新闻标签--------------------------------------------------------------------
class News_tag(models.Model):
    name = models.CharField(max_length=10)
    rank = models.IntegerField(default=99)

    def __str__(self):
        return self.name
        ordering = ['rank']

    def get_tag_url(self):
        return reverse('tag', args=(self.name, ))

    class Meta:
        verbose_name_plural = 'C1_新闻标签'


class News_tag_admin(admin.ModelAdmin):
    list_display = ('name', 'rank')


admin.site.register(News_tag, News_tag_admin)


# 新闻来源-------------------------------------------------------------------------
class Origin(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'C2_新闻来源'


class Origin_admin(admin.ModelAdmin):
    list_display = ('name', 'url')


admin.site.register(Origin, Origin_admin)


# 新闻内容-------------------------------------------------------------------------
class News(models.Model):
    IS_TOP_CHOICES = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    title = models.CharField(max_length=50)
    IS_TOP = models.CharField(
        max_length=5, choices=IS_TOP_CHOICES, default='N')
    news_tag = models.ManyToManyField(News_tag)
    origin = models.ForeignKey(Origin,on_delete=models.CASCADE)
    main_img = models.ImageField(upload_to='news_main_img', blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    # published_date2 = models.CharField(default = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),max_length = 50)
    content = UEditorField('内容', height=300, width=1000, default=u'', blank=True,
                           imagePath='news_img/', toolbars='besttome', filePath='news_files/')

    def __str__(self):
        return self.title

    # 得到文章摘要，此方法效率低。可以用更好的方法来实现，如重写save()方法，或直接创建一个关于摘要的字段。
    def get_news_abstract(self):
        # 匹配html tag 及其中的内容，如<div class='box'>。<不含 > 的字符，1次或多次>
        RE_ABSTRACT = r'<[^>]+>'
        # compile regular expression patten into a regular expression object
        pattern = re.compile(RE_ABSTRACT)
        # print(pattern.sub('',self.content[0:300]))
        return pattern.sub('', self.content[0:500])  # 用空内容取消html标签及其中的内容

    def get_news_url(self):
        return reverse('news-detail', args=(self.pk,))

    class Meta:
        verbose_name_plural = 'C3_新闻内容'
        ordering = ['-published_date']


class News_admin(admin.ModelAdmin):
    list_display = ('title', 'origin', 'published_date', 'IS_TOP')


admin.site.register(News, News_admin)


# 新闻评论----------------------------------------------------------------------------
class News_comment(models.Model):
    news_title = models.ForeignKey(News,on_delete=models.CASCADE)
    comment = models.ForeignKey(Reg_user,on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField(blank=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name_plural = ('C4_新闻评论')
        ordering = ['-comment_time']


class News_comment_admin(admin.ModelAdmin):
    list_display = ('news_title', 'comment_time', 'comment_text')


admin.site.register(News_comment, News_comment_admin)


# 博客标签----------------------------------------------------------------------------
class Blog_tag(models.Model):
    name = models.CharField(max_length=10)
    tag_img = models.FileField(upload_to='tag_img', blank=True)
    rank = models.IntegerField(default=99)

    def __str__(self):
        return self.name
        ordering = ['rank']

    def get_tag_url(self):
        return reverse('tag', args=[self.name])

    class Meta:
        verbose_name_plural = 'D1_博客标签'


class Blog_tag_admin(admin.ModelAdmin):
    list_display = ('name', 'tag_img', 'rank')


admin.site.register(Blog_tag, Blog_tag_admin)


# 博客内容-----------------------------------------------------------------------------
class Blog(models.Model):
    IS_TOP_CHOICES = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    IS_TOP = models.CharField(
        max_length=5, choices=IS_TOP_CHOICES, default='N')
    title = models.CharField(max_length=100)
    blog_author = models.ForeignKey(Reg_user,on_delete=models.CASCADE)
    blog_tag = models.ManyToManyField(Blog_tag, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    main_img = models.ImageField(upload_to='blog_main_img', blank=True)
    content = UEditorField('内容', height=300, width=1000, default=u'', blank=True,
                           imagePath='blog_content_img/', toolbars='besttome', filePath='blog_files/')
    blog_click = models.IntegerField(default=0)
    blog_love = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'D2_博客内容'
        ordering = ['-IS_TOP', '-published_date']

    def get_blog_abstract(self):
        RE_ABSTRACT = r'<[^>]+>'
        pattern = re.compile(RE_ABSTRACT)
        return pattern.sub('', self.content[0:300])

    def get_blog_url(self):
        return reverse('blog-detail', args=(self.pk,))


class Blog_admin(admin.ModelAdmin):
    list_display = ('title', 'blog_author', 'IS_TOP', 'published_date')


admin.site.register(Blog, Blog_admin)


# 博客评论----------------------------------------------------------------------------
class Blog_comment(models.Model):
    blog_title = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.ForeignKey(Reg_user, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField(blank=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name_plural = ('D3_博客评论')
        ordering = ['-comment_time']


class Blog_comment_admin(admin.ModelAdmin):
    list_display = ('blog_title', 'comment_time', 'comment_text')


admin.site.register(Blog_comment, Blog_comment_admin)


# 分享标签------------------------------------------------------------------------
class Share_tag(models.Model):
    tag_name = models.CharField(max_length=10)
    rank = models.ImageField(default=99)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name_plural = ('E1_分享标签')
        ordering = ['-rank']


class Share_tag_admin(admin.ModelAdmin):
    list_display = ('tag_name', 'rank')


admin.site.register(Share_tag, Share_tag_admin)


# 分享文件-------------------------------------------------------------------------
class Share_file(models.Model):
    share = models.ForeignKey('Share',on_delete = models.CASCADE)
    share_file = models.FileField(upload_to='share_file', blank=True)

    class Meta:
        verbose_name_plural = ('E2_分享文件')

    def get_file_name(self):
        return self.share_file.name.split('/')[-1]


class Share_file_admin(admin.ModelAdmin):
    list_display = ('share', 'share_file',)


admin.site.register(Share_file, Share_file_admin)


# 分享----------------------------------------------------------------------------
class Share(models.Model):
    author = models.ForeignKey(Reg_user,on_delete = models.CASCADE)
    share_title = models.CharField(max_length=20, blank=True)
    share_time = models.DateTimeField(auto_now_add=True)
    share_desc = models.TextField(blank=True)
    share_tag = models.ManyToManyField(Share_tag)

    def __str__(self):
        return self.share_title

    def show_tag(self):
        return ",".join([t.tag_name for t in self.share_tag.all()])
    show_tag.short_description = 'tag'

    class Meta:
        verbose_name_plural = ('E3_分享')


class Share_admin(admin.ModelAdmin):
    list_display = ('author', 'share_title', 'share_time',
                    'share_desc', 'show_tag')


admin.site.register(Share, Share_admin)


# 反馈----------------------------------------------------------------------------
class Feedback(models.Model):
    feedback_content = models.CharField(max_length=300)
    feedback_contact = models.CharField(max_length=100, blank=True)
    feedback_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback_content

    class Meta:
        verbose_name_plural = ('F1_反馈')


class Feedback_admin(admin.ModelAdmin):
    list_display = ('feedback_content', 'feedback_contact', 'feedback_time')


admin.site.register(Feedback, Feedback_admin)


# 附加信息---------------------------------------------------------------
class Addtional_info(models.Model):
    content = models.CharField(max_length=32, blank=True)

    class Meta:
        verbose_name_plural = 'G1_附加信息'


class Addtional_info_admin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(Addtional_info, Addtional_info_admin)
