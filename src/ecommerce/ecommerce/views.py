from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,"home_page.html", {})

#this one is having a seperate folder

def about_page(request):
    return render(request,"home_page.html", {})

def contact_page(request):
    context = {
    "title": "this is contact page"
    }
    if request.method == "POST":
        #print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request,"contacts/views.html", context)

# def home_page(request):
#     return render(request,"auth/login.html", {})
#
# def home_page(request):
#         return render(request,"auth/register.html", {})
