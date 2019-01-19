# -*- coding: utf-8 -*-

import random

from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import Change_pw_form, UserForm
from .models import Reg_user

# 注册、登录用自己写的方法，未用django自带的。

# 注册页


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            try:
                is_register = Reg_user.objects.get(username=username)
            except:
                add_register = Reg_user.objects.create(
                    username=username,
                    password=make_password(password),
                    email=email)
                request.session['session_username'] = username
                # session_username = request.session.get('session_username')
                return render(request, 'user_admin/success-reg.html', locals())
    else:
        uf = UserForm()
    return render(request, 'user_admin/register.html', locals())


# 登录页
def login(request):
    if request.method == 'POST':
        # post提交的，隐藏表单里的from_url，即post提交前的一个url
        from_url = request.POST.get('from_url')
        if from_url in ['', 'http://' + request.META['HTTP_HOST'] + '/register/',
                        'http://' + request.META['HTTP_HOST'] + '/login/']:
            from_url = '/'
        uf = UserForm(request.POST)
        # print(uf.is_valid())          # false。不用 is_valid()，是因为form里有4个字段，而这里只用2个，false。
        if uf.is_bound:
            # print('is_bound', uf.is_bound)    # true
            a = uf.is_valid()                   # 只有验证后，才能使用cleaned_data方法，即使是验证 false。
            # print('is_valid', a)              # false
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            has_username = Reg_user.objects.filter(username=username)
            if has_username:
                get_password = has_username[0].password
                check_pw = check_password(password, get_password)
                if check_pw:
                    request.session['session_username'] = username
                    return redirect(from_url)
                else:
                    is_login = False
                    return render(request, 'user_admin/login.html', locals())
            else:
                is_login = False
                return render(request, 'user_admin/login.html', locals())
        else:
            is_login = False
            return render(request, 'user_admin/login.html', locals())
    else:
        uf = UserForm()
        return render(request, 'user_admin/login.html', locals())


# ajax，登录页，检查用户名
@csrf_exempt
def ajax_check_username(request):
    # print(request.POST)
    try:
        username = Reg_user.objects.get(username=request.POST['username'])
    except:
        username = False
    return HttpResponse(username)


# 登出
def logout(request):
    # del request.session['session_username']
    # 注意与放在隐藏表单里的HTTP_REFERER的区别。META里的值会自动变化，
    from_url = request.META.get('HTTP_REFERER')
    # 如不放在表单里POST保存，当login跳转后，值就成了/login/。登出只是一个按钮，没有页面，用META里的值就够了。
    request.session.flush()                     # django login的使用方法。
    response = redirect(from_url)
    return response

 # 用户详情页


def useradmin_base(request):
    user = useradmin_base_common(request)
    return render(request, 'useradmin_base.html', locals())


# 修改密码
def useradmin_change_password(request):
    user = useradmin_base_common(request)
    if request.method == 'POST':
        change_pw_form = Change_pw_form(request.POST)
        if change_pw_form.is_valid():
            password_old = change_pw_form.cleaned_data['password_old']
            password_new = change_pw_form.cleaned_data['password_new']
            # password_new_yz = change_pw_form.cleaned_data['password_new_yz']      #用ajax验证

            user_pw = user.password
            print(user_pw)
            check_pw = check_password(password_old, user_pw)
            if check_pw:
                user.password = make_password(password_new)
                user.save()
                PW_ERROR_INFO = '密码修改成功'
                # return redirect("/useradmin/")
            else:
                PW_ERROR_INFO = '原密码错误'
        else:
            change_pw_form = Change_pw_form()
    else:
        change_pw_form = Change_pw_form()
    return render(request, 'user_admin/useradmin_change_password.html', locals())


# 修改邮箱
def useradmin_change_email(request):
    user = useradmin_base_common(request)
    if request.method == 'POST':
        print(request.POST)
        old_email = request.POST['old-email']
        new_email = request.POST['new-email']
        yzm = request.POST['yzm']
        if yzm == request.session.get('yzm_session'):
            user.email = new_email
            user.save()
            email_info = 'Ture'
    return render(request, 'user_admin/useradmin_change_email.html', locals())


# 用 ajax 验证旧邮箱是否正确
@csrf_exempt
def ajax_check_old_email(request):
    user = useradmin_base_common(request)
    print(user.email)
    if user.email == request.POST['old_email']:
        return HttpResponse('True')
    else:
        return HttpResponse('False')


# 用 ajax 设置验证码及用邮箱发送
@csrf_exempt
def ajax_send_yzm(request):
    print(request.POST)
    new_email = request.POST['new_email']
    print(new_email)
    yzm_random = ('').join(random.sample("123456789", 4))
    request.session['yzm_session'] = yzm_random
    print(yzm_random)
    send_mail(
        '麦星科技验证码',
        '您的验证码为：' + yzm_random,
        'admin@innocosme.com',     # settings 里设置的发件箱
        (new_email,),    # 收件箱
        fail_silently=False
    )
    return HttpResponse("True")


# 在user_admin app中，很多view要以useradmin_base view为基础，故封装useradmin_base函数
def useradmin_base_common(request):
    session_username = request.session.get('session_username')
    if session_username:
        user = Reg_user.objects.get(username=session_username)
        return user
