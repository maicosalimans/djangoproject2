from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm
from .forms import PollForm
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_inhoud.html', {'post': post})

def post_nieuw(request):   # dit was post_nieuw
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_nieuw(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_inhoud', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def delete_post(request,post_id=None):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def poll_view(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data
            answer = form.cleaned_data['question']
            #You can save the answer to the database or procedd it as needed
            return render(request, 'blog/thanks.html', {'answer': answer})
    else:
        form = PollForm()

    return render(request, 'blog/poll.html', {'form': form})

