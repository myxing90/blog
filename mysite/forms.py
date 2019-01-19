# -*- coding: utf-8 -*-

from django import forms

class CommentForm(forms.Form):
    '''
    评论表单
    '''
    comment_text = forms.CharField(max_length=200,
                                   widget=forms.Textarea(attrs={
                                       'class': 'comment-text',
                                       'placeholder': '请登录后评论,最多200字',
                                   }))
