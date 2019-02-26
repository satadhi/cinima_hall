from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    return render(request,"home_page.html", {})

#this one is having a seperate folder

def about_page(request):
    return render(request,"home_page.html", {})

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
    "title": "this is contact page",
    "form" : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
        #print(request.POST)
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))
    return render(request,"contacts/views.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
                "form" : form

        }
    print("user login is:")
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated())

        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("error !! ")

    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
                "form" : form

        }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
    return render(request,"auth/register.html",context)

# def home_page(request):
#     return render(request,"auth/login.html", {})
#
# def home_page(request):
#         return render(request,"auth/register.html", {})
