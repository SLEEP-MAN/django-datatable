#!/usr/bin/env python
# coding: utf-8
from django.conf.urls import include, url

from app import views


urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^filterable/$', views.filterable, name='filterable'),
    url(r'^datasource/ajax/$', views.ajax, name='ajax'),
    url(r'^datasource/ajaxsource/$', views.ajax_source, name='ajax_source'),
    url(r'^datasource/ajaxsource/api/$', views.MyDataView.as_view(), name='ajax_source_api'),

    url(r'^column/sequence/$', views.sequence_column, name='sequence_column'),
    url(r'^column/calendar/$', views.calendar_column, name='calendar_column'),
    url(r'^column/link/$', views.link_column, name='link_column'),
    url(r'^column/checkbox/$', views.checkbox_column, name='checkbox_column'),

    url(r'^user/(\d+)/$', views.user_profile, name='user_profile'),
    url(r'^table/', include('table.urls')),
]
