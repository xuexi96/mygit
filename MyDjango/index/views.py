#coding=utf-8
from django.shortcuts import render,HttpResponse

# Create your views here.
# def index(request):
#     return render(request,'index.html')
#
# def myvariable(request,year,month,day):
#      return HttpResponse(str(year)+"/"+str(month)+"/"+str(day))
#
# def index2(request,month):
#     return HttpResponse("路由外的url变量"+month)

#-----------------------------------------------------------
#路由命名
# def index(request,year):
#     return render(request,'index.html')


#模板中使用路由
#------------------------------------------------------------------
# def mydate(request,year,month,day):
#     return HttpResponse(str(year)+"/"+str(month)+"/"+str(day))
#
# def index(request):
#     return render(request,"index.html")
#---------------------------------------------------------------------

