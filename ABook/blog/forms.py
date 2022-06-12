from django import forms

from .models import Post
from django.shortcuts import render
from django.shortcuts import redirect
#from ABook.blog.forms import PostForm
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import get_object_or_404

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})