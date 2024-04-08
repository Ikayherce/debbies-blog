from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic 
from django.views.generic import CreateView, UpdateView, DeleteView   #test line 
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy, reverse  #test line


def LikeView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # Check if the post is already liked by the user
    if post.likes.filter(id=request.user.id).exists():
        # User has already liked this post, so unlike it
        post.likes.remove(request.user)
    else:
        # User has not liked this post yet, so like it
        post.likes.add(request.user)
    
    # Redirect to the post's detail page
    return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
    

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):


    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()


    return render(
    request,
    "blog/post_detail.html",
    {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
)

def CategoryView(request, cats):
    cats_lower = cats.lower()
    try:
        category = Category.objects.get(name__iexact=cats_lower)
        category_posts = Post.objects.filter(category=category)
    except Category.DoesNotExist:
        category_posts = Post.objects.none()  # Empty queryset
    
    return render(request, 'categories.html', {'cats': cats, 'category_posts': category_posts})


#test code below for category view
#def CategoryView(request, cats):
#    cats_lower = cats.lower() #test 
#    try:
#        category = Category.objects.get(name=cats)
#        category_posts = Post.objects.filter(category=category)
#    except Category.DoesNotExist:
#        # Handle the case when the category does not exist
#        # You can return an empty queryset or render an error page
#        category_posts = Post.objects.none()  # Empty queryset
    
#    return render(request, 'categories.html', {'cats': cats, 'category_posts': category_posts})



#test code below for category view
#def CategoryView(request, cats):
#    category_posts = Post.objects.filter(category=cats)
#    return render(request,'categories.html',{'cats':cats,'category_posts':category_posts})

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))



def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPostView(CreateView):
    model = Post 
    form_class = PostForm #testcode
    template_name = 'add_new_post.html'
   # fields = '__all__'

#test for adding category from website
class AddCategoryView(CreateView):
    model = Category 
    #form_class = PostForm #testcode
    template_name = 'add_category.html'
    fields = '__all__'


#test code for update post page
class UpdatePostView(UpdateView): 
    model = Post
    form_class = PostForm #testcode
    template_name = 'update_post.html' 
    #fields = ['title', 'content', 'excerpt', 'category', 'featured_image', 'status']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html' 
    success_url = reverse_lazy('home')

