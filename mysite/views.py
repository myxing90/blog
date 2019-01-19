# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from .forms import CommentForm
from django.db.models import Count
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from common_functions.my_paginator import common_paginator

# 主页


def index(request):
    top_url = Top_url.objects.all()
    sort_tag = Sort_tag.objects.all()
    blog_hot = Blog.objects.filter(IS_TOP='Y')
    news_tag_list = News_tag.objects.annotate(
        arcticle_num=Count('news')).order_by('-arcticle_num')[:12]
    blog_tag_list = Blog_tag.objects.annotate(
        arcticle_num=Count('blog')).order_by('-arcticle_num')[:12]
    news = News.objects.annotate(comment_num=Count(
        'news_comment')).order_by('-comment_num')[:4]
    blog = Blog.objects.annotate(comment_num=Count(
        'blog_comment')).order_by('-comment_num')[:6]
    share = Share.objects.all()[:4]
    return render(request, 'mysite/index.html', locals())


# 新闻主页
def news_index(request):
    comment_num = News.objects.annotate(comment_num=Count(
        'news_comment')).order_by('-comment_num')[:5]
    news_tag = News_tag.objects.all()

    news_list = News.objects.all()
    news = common_paginator(request, news_list, 5)
    return render(request, 'mysite/news-index.html', locals())


# 新闻详情页
def news_detail(request, pk):
    session_username = request.session.get('session_username')
    now_url = request.path
    news = News.objects.get(pk=pk)
    news_tag_list = News_tag.objects.filter(news__pk=pk)
    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
            author = Reg_user.objects.get(username=session_username)
            add_comment = News_comment.objects.create(news_title=news, comment=author,
                                                      comment_text=cf.cleaned_data['comment_text'])
            response = redirect(now_url + '#newsdetail-comment')
            return response
    else:
        cf = CommentForm()

    return render(request, 'mysite/news-detail.html', locals())


# 博客主页
def blog_index(request):
    blog_tag = Blog_tag.objects.all()
    comment_num = Blog.objects.annotate(comment_num=Count(
        'blog_comment')).order_by('-comment_num')[:5]
    blog_num = Reg_user.objects.annotate(
        blog_num=Count('blog')).order_by('-blog_num')[:5]
    blog_list = Blog.objects.filter(IS_TOP='N')
    blog = common_paginator(request, blog_list, 5)
    return render(request, 'mysite/blog-index.html', locals())


# 博客详情页
def blog_detail(request, pk):
    session_username = request.session.get('session_username') 
    now_url = request.path
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        author = Reg_user.objects.get(username=session_username)
        cf = CommentForm(request.POST)
        if cf.is_valid():
            blog_title = Blog.objects.get(pk=pk)
            add_comment = Blog_comment.objects.create(blog_title=blog_title, comment=author,
                                                      comment_text=cf.cleaned_data['comment_text'])
            response = redirect(now_url + '#blogdetail-comment')
            return response
    else:
        cf = CommentForm()
    return render(request, 'mysite/blog-detail.html', locals())


# 标签页
def tag(request, tag):
    try:
        news_tag = News_tag.objects.get(name=tag)
    except:
        try:
            blog_tag = Blog_tag.objects.get(name=tag)
        except:
            author_tag = Reg_user.objects.get(username=tag)

    if request.method == 'POST':
        author = Reg_user.objects.get(username=username)
        cf = CommentForm(request.POST)
        if cf.is_valid():
            blog_title = Blog.objects.get(pk=pk)
            add_comment = Blog_comment.objects.create(blog_title=blog_title, comment=author,
                                                      comment_text=cf.cleaned_data['comment_text'])
            response = redirect(now_url + '#blogdetail-comment')
            return response
    else:
        cf = CommentForm()
    return render(request, 'mysite/tag.html', locals())


# 分享页
def share_index(request):
    share_list = Share.objects.all()
    return render(request, 'mysite/share-index.html', locals())


# ajax，反馈功能，发邮件
@csrf_exempt
def ajax_feedback(request):
    # print(request.POST)
    feedback_content = request.POST['feedback_content']
    feedback_contact = request.POST['feedback_contact']
    # print(feedback_content)
    # print(feedback_contact)
    if feedback_content:
        feedback = Feedback.objects.create(
            feedback_content=feedback_content, feedback_contact=feedback_contact)
        send_mail(
            'blog-反馈信息',
            feedback_contact+'\n'+feedback_content,
            'admin@xxx.com',
            ['xxx@qq.com'],
            fail_silently=False
        )
    else:
        return HttpResponse(False)
    return HttpResponse(True)
