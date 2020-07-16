from django.shortcuts import render, redirect

from .models import Comment
from .forms import CommentForm, CommentModelForm


def index(request):
    comments = Comment.objects.order_by('-date_added')
    context = {
        'comments': comments
    }
    return render(request, 'guestBook/index.html', context)


def sign(request):
    if request.method == 'POST':
        form = CommentModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommentModelForm()
    #     form = CommentForm(request.POST or None)
    #     if form.is_valid():
    #         # comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
    #         comment = Comment.objects.create(name=request.POST['name'], comment=request.POST['comment'])
    #         # comment.save()
    #         return redirect('index')
    # else:
    #     form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'guestBook/sign.html', context)