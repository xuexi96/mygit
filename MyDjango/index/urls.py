#coding=utf-8
from django.urls import path,re_path
# index.views import index           # myvariable,index2,
from index import views

urlpatterns = [

#----------------------------------------------------------------
    #路由变量（字符类型、整型、slug、uuid）
    # 变量符号<>
    #path("<year>/<int:month>/<slug:day>",myvariable),
    #path("",index2,{"month":"2021/05/16"})
    #正则表达式url
    #使用re_path
    #re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})",myvariable)
    # ?P是固定格式
    #  <year>是变量
    #  [0-9]{4}是正则匹配模式


#-----------------------------------------------------------------------
    #在模板中使用路由
    # path("<year>/<int:month>/<slug:day>",views.mydate,name="mydata"),
    # path("",views.index),
    # path("v",views.v)
#-----------------------------------------------------------------------

]