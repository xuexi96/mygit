#coding=utf-8
"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
#from index.views import index


#--------------------------------------------------------------------
#配置媒体文件夹
from django.views.static import serve
from django.conf import settings


#---------------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),


#---------------------------------------------------------------------

    #命名空间设置include(age,namespace)
    #age是用于指向app的参数，这个参数可以是字符串或元组，namespace是可选参数，是路由的命名空间，若设置namespace则age必须为元组元组的长度必须为二
    #元组的第一个元数app下的url文件，第二个元数可以随便命名但不能为空
    # path("",include(("index.urls",'index'),namespace='index')),
    #path("user/",include(('user.url','user'),namespace='user')),


#-----------------------------------------------------------------------
    #命名空间
    path("",include("index.urls")),
    #path("",include("index.html")),
    #path("",include(("index.urls","index"),namespace="index")),

#------------------------------------------------------------------------
    #配置媒体文件的路由地址
    re_path("media/(?P<path>.*)",serve,{'document_root':settings.MEDIA_ROOT},name="media")


#------------------------------------------------------------------------
    #反向解析reverse 与 

]
