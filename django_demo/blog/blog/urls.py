# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.views import RSSFeed

urlpatterns = patterns('',
                       # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'article.views.home'),

    url(r'^$', 'article.views.home', name='home'),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archives/$', 'article.views.archives', name='archives'),
    url(r'^aboutme/$', 'article.views.about_me', name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', 'article.views.search_tag', name='search_tag'),
    url(r'^search/$', 'article.views.blog_search', name='search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"),  #新添加的urlconf, 并将name设置为RSS, 方便在模板中使用url

    # url(r'^$', 'article.views.home'),  # 由于目前只有一个app, 方便起见, 就不设置include了
    # url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),
    # ^(?P<my_args>\d+)/$这个正则表达式的意思是将传入的一位或者多位数字作为参数传递到views中的detail作为参数,
    #  其中?P<my_args>定义名称用于标识匹配的内容

    # url(r'^test/$', 'article.views.test'),
)
