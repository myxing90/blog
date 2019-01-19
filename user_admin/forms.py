# -*- coding: utf-8 -*-

from django import forms


class UserForm(forms.Form):
    '''
    用户表单，注册和登录用同一个表单。
    '''
    username = forms.CharField(label='用户名', max_length=10, min_length=3,
                               error_messages={'required': 'Dear,请输入用户名,最少3位,最多10位',
                                               'max_length': 'Dear,请输入用户名,最少3位,最多10位',
                                               'min_length': 'Dear,请输入用户名,最少3位,最多10位'},
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名,最少3位'
                                                             }))

    password = forms.CharField(label='密 码', max_length=10, min_length=4,
                               error_messages={'required': 'Dear,请输入密码,最少4位,最多10位',
                                               'max_length': 'Dear,请输入密码,最少4位,最多10位',
                                               'min_length': 'Dear,请输入密码,最少4位,最多10位'},
                               widget=forms.PasswordInput(attrs={'placeholder': '请输入密码,最少4位数字或字母'
                                                                 }))

    password_yz = forms.CharField(label='确认密码', max_length=10, min_length=4,
                                  # error_messages = {'required':'Dear,请输入密码,最少4位,最多10位',
                                  # 				'max_length':'Dear,请输入密码,最少4位,最多10位',
                                  # 				'min_length':'Dear,请输入密码,最少4位,最多10位'},
                                  widget=forms.PasswordInput(attrs={'placeholder': '请重复密码'
                                                                    }))

    email = forms.EmailField(label='邮 箱', max_length=50,
                             # error_messages = {'invalid':'Dear,邮箱格式不正确'},
                             widget=forms.EmailInput(attrs={'placeholder': '电子邮箱,用于找回密码'
                                                            }))


class Change_pw_form(forms.Form):
    '''
    修改密码，使用forms.form练习
    '''
    password_old = forms.CharField(label='旧密码', max_length=10, min_length=4,
                                   widget=forms.PasswordInput(attrs={'placeholder': '请输入旧密码'}))

    password_new = forms.CharField(label='新密码', max_length=10, min_length=4,
                                   widget=forms.PasswordInput(attrs={'placeholder': '请输入新密码,最少4位数字或字母'
                                                                     }))
    password_new_yz = forms.CharField(label='确认新密码', max_length=10, min_length=4,
                                      widget=forms.PasswordInput(attrs={'placeholder': '请重复新密码'
                                                                        }))


class Change_email(forms.Form):
    '''
    用   HTML    FORM    练习
    '''
    pass
    