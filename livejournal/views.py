from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

# Create your views here.

class PostList(TemplateView):
    template_name = 'livejournal/post_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return context

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

'''        
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('livejournal.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'livejournal/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('livejournal.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'livejournal/post_edit.html', {'form': form})

'''