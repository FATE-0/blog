# coding=gbk

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea �����̨'
    index_title = '��ҳ'
    
custom_site = CustomSite(name='cus_admin')
