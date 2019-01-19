from django.core.paginator import Paginator

def common_paginator(request, contact_list, per_page_num):
    '''
    为不重复工作，自定义通用分页函数
    '''
    paginator = Paginator(contact_list, per_page_num)
    page = request.GET.get('page', 1)
    try:
        contact = paginator.page(page)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        contact = paginator.page(1)
    return contact