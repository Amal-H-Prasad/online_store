from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from store.encrypt_util import *
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model


def index(request):
    return render(request, 'index.html')

def user_add_review(request):
    return render(request,'user_add_review.html')

def admin_home(request):
    return render(request, "admin_home.html")


def user_home(request):
    return render(request, "user_home.html")


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def checkout(request):
    return render(request, 'checkout.html')


def profile(request):
    return render(request, 'Myprofile.html')


def passwordchange(request):
    return render(request, 'passwordchange.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
            else:
                user = User(first_name=firstname, last_name=lastname,
                            email=email, username=username, password=password1)
                user.save()
                messages.info(request, "User Created")
        else:
            messages.info(request, "Password Not Match")
            return redirect('register')
        return redirect('login')
    else:
        return render(request, 'register.html')


# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         if User.objects.filter(username=username, password=password):
#             data = User.objects.get(username=username, password=password)
#             if data.username == "amal":
#                 template = loader.get_template('admin_home.html')
#                 context = {}
#                 return HttpResponse(template.render(context, request))
#             elif data.username != "amal":
#                 template = loader.get_template('user_home.html')
#                 context = {}
#                 return HttpResponse(template.render(context, request))
#             else:
#                 data = User.objects.get(username=username)
#                 if data.is_active == False:
#                     messages.info(request, "User is inactive")
#                 else:
#                     request.session["username"] = username
#                     return redirect('/')
#         else:
#             return redirect('login')
#     return render(request, 'login.html')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username,password=password):
            data=User.objects.get(username=username,password=password)
            if data.username!="admin":
                request.session['username']=data.username
                template = loader.get_template('user_home.html')
                context = {'session':request.session['username']}
                return HttpResponse(template.render(context,request))
            elif data.username=="admin":
                template = loader.get_template('admin_home.html')
                context = {}
                return HttpResponse(template.render(context,request))
            else:
                return redirect('/userhome')

    return render(request,'login.html')



def forgetpassword(request):
    if request.method == "POST":
        username = request.POST['username']
        data = User.objects.get(username=username)
        if data:
            password = request.POST['newpassword']
            cpassword = request.POST['conpassword']
            if password == cpassword:
                data.password = password
                data.save()
                messages.info(request, "password reset successsfully")
                return redirect('login')
            else:
                return HttpResponse("<script> alert('Password Mismatch');window.location='/forgetpassword';</script>")
    return render(request, 'passwordchange.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def viewuser(request):
    username=request.session['username']
    data = User.objects.get(username=username)
    template = loader.get_template('MyProfile.html')
    context = {'data':data}
    return HttpResponse(template.render(context,request))

def admin_view_user(request):
    user = get_user_model()
    data = user.objects.all()
    template = loader.get_template('admin_view_user.html')
    context = {'data':data}
    return HttpResponse(template.render(context, request))


def edituser(request,id):
        data=User.objects.get(id=id)
        request.session['id']=id
        template = loader.get_template('edituser.html')
        context = {'data':data}
        return HttpResponse(template.render(context,request))

def edituser1(request):
    id=request.session['id']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    username = request.POST['username']
    data=User.objects.get(id=id)
    data.first_name=first_name
    data.last_name=last_name
    data.email=email
    data.username=username
    data.save()
    data=User.objects.get(id=id)
    template = loader.get_template('MyProfile.html')
    context = {'data':data}
    return HttpResponse(template.render(context,request))

def deleteuser(request,id):
    data = User.objects.get(id=id)
    request.session['id'] = id
    template = loader.get_template('deleteuser.html')
    context = {'data': data}
    data.delete()
    return HttpResponse(template.render(context, request))
# def deleteuser1(request,id):
#     data=User.objects.get(id=id)
#     request.session['id'] = id
#     data.delete()
#     return redirect('register')
#     return render(request,'register.html')



def user_add_review(request,id):
    # if request.method == "POST":
    #     user_id = request.session['id']
    #     Review = request.POST['Review']
    #     reply = ' '
    #   # Date=datetime.today().strftime('%Y-%m-%d')
    #     data = user_review(Review=Review, reply=reply, user_id=user_id)
    #     data.save()
    return render(request, 'user_add_review.html')