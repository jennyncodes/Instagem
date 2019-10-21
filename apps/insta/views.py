from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Message, Comment
from datetime import datetime
import bcrypt


#first page
def index(request):
    if 'id' in request.session.keys():
        request.session.clear()
    if 'first_name' not in request.session.keys():
        request.session['first_name'] = ''
        request.session['last_name'] = ''
        request.session['email'] = ''
        request.session['lemail'] = ''
    return render(request,"insta/instagem.html")

#login page
def login(request):
    return render(request, "insta/instagem.html")

#login form
def logform(request):
    errors = User.objects.login_validator(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request,value, extra_tags = key)
            return redirect('/')
        request.session['id'] = User.objects.get(email=request.POST['lemail']).id
        request.session['first_name'] = User.objects.get(email=request.POST['lemail']).first_name
    return redirect('/profile')    

#registeration page
def register(request):
    return render(request, "insta/register.html")
    
#registration form
def registration(request):
    print (request.POST)
    errors = User.objects.basic_validator(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request,value, extra_tags = key)
            return redirect('/register')
        else:
            User.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
            request.session['id'] = User.objects.last().id
            request.session['first_name'] = User.objects.last().first_name
            return redirect('/profile')
    return redirect('/profile')

#user's page
def profile(request):
    all_message = Message.objects.all()
    all_user = User.objects.all()
    all_comment = Comment.objects.all()
    context= {
		'all_message': all_message,
		'all_user': all_user,
        'all_comment': all_comment
	    }
    return render(request, "insta/profile.html", context)

def create(request):
    Message.objects.create(message=request.POST['add_message'], user= User.objects.get(id=request.session['id']))
    return redirect('/profile')

def create_comment(request):
    Comment.objects.create(comment = request.POST['posting'], user = User.objects.get(id=request.session['id']), message = Message.objects.get(id=request.POST['mid']))
    return redirect('/profile')


# def add_message(request):
# 	Message.objects.create(message=request.POST['add_message'], user=User.objects.get(first_name=request.session['first_name']))
# 	return redirect("/profile")

def delete_message(request):
	message= Message.objects.get(id=request.POST['mid']).delete()
	return redirect("/profile")

def comment(request):
	Comment.objects.create(comment=request.POST['comment'], user=User.objects.get(id=request.POST['id']), message=Message.objects.get(id=request.POST['message_ID']))
	return redirect("/profile")

#logout
def logout(request):
	request.session.clear()
	return redirect('/')