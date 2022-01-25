from django.contrib import messages
from django.shortcuts import render, redirect
from .models import About, Offers, Teams, Contact
from blog.models import Post, User


def index(request):
    MyAbout = About.objects.get(id=1)
    offers = Offers.objects.all()
    teams = Teams.objects.all()
    blogs = Post.objects.all()[:3]
    if request.method == 'POST':
        if request.POST.get('Email') and request.POST.get('Subject') and request.POST.get(
                'Body'):
            savemessage = Contact()
            savemessage.Email = request.POST['Email']
            savemessage.Subject = request.POST['Subject']
            savemessage.Body = request.POST['Body']
            savemessage.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('index')
        else:
            print('Something went wrong')
            return redirect('index')

    return render(request, 'index.html', {'MyAbout': MyAbout, 'offers': offers, 'teams': teams, 'blogs': blogs})
# Create your views here.