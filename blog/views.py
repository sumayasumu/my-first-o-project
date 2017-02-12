from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import clientaccount
from .forms import accountform
from django.shortcuts import redirect
@login_required
def index(request):
    return render(request, 'blog/index.html', {})

def deposit(request):
    return render(request, 'blog/deposit.html', {})


def widraw(request):
    return render(request, 'blog/widraw.html', {})


def post_list(request):
    posts = clientaccount.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def account_new(request):
    if request.method == "POST":
        form = accountform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog/index', pk=post.pk)
    else:
        form = accountform()
    return render(request, 'blog/post_edit.html', {'form': form})
# Create your views here.
