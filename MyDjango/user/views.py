from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is userIndex")


def userLogin(requts):
    return HttpResponse("This is userLogin")
