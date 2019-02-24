from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,"home_page.html", {})

#this one is having a seperate folder
def contact_page(request):
    context = {
    "title": "this is contact page"
    }
    return render(request,"contacts/views.html", context)

def about_page(request):
    return render(request,"home_page.html", {})


# def home_page(request):
#     return render(request,"auth/login.html", {})
#
# def home_page(request):
#         return render(request,"auth/register.html", {})
