from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from blog.models import Post
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsLetterForm
from django.contrib import messages


def index_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request,'website/index.html',context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Ticket submitted successfully')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didn't submit.")
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def about_view(request):
    return render(request, 'website/about.html')

def home_view(request):
    return render(request, 'website/index-2.html')

def blog_view(request):
    return render(request, 'blog/blog.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Email submitted successfully')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

    