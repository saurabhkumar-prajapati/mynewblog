from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUPForm, LogInForm, PostForm
from django.contrib import messages
from .models import Post
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


# Home View
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


# about view
def about(request):
    return render(request, 'blog/about.html')

    # contact view
    # def contact(request):
    return render(request, 'blog/contact.html')


# dashboard view
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts': posts, 'full_name': full_name, 'groups': gps})
    else:
        return HttpResponseRedirect("/login/")


# logout view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# signup view
def user_signup(request):
    if request.method == 'POST':
        form = SignUPForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations  ! on becoming an author")
            user = form.save()
            group = Group.objects.get(name='myauthor')
            user.groups.add(group)
    else:
        form = SignUPForm()

    return render(request, 'blog/signup.html', {'form': form})


# login view
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LogInForm(request.POST, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return HttpResponseRedirect('/dashboard/')  # in ursls.py file right side url

        else:
            form = LogInForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


# add new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                form = PostForm()
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})
    else:
        HttpResponseRedirect('/login/')


# update post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, "blog/updatepost.html", {'form': form})
    else:
        HttpResponseRedirect('/login/')


# delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        HttpResponseRedirect('/login/')


# contact form
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = request.POST['email_address']
            subject = "Internship/Job Offer"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'contact_number':form.cleaned_data['contact_number'],
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
           #try:
            send_mail(subject, message, email, ['saurabhcs0087@gmail.com'])
            messages.success(request, "Thanks message send successfuly")
            #except BadHeaderError:
                #return HttpResponse('Invalid header found.')
            return HttpResponseRedirect("/contact/")
    else:
        form = ContactForm()

    return render(request, "blog/contact.html", {'form': form})
