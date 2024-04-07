from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse #test
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
#code below is test code for category model
class Category (models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):                   
        return reverse('home')  

#end of test code for category model


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts') # code for likes
    category =  models.ForeignKey(Category, on_delete=models.CASCADE) #test code for categories

    def total_likes(self):          # code to display likes 
        return self.likes.count()    # code to display likes 

    class Meta: 
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def get_absolute_url(self):   
        #return reverse('post_detail', kwargs={'slug': self.slug})   #redirect to post                  
        return reverse('home') #or redirect home?
    
    #test code to generate slug if not specified 
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if not provided
            self.slug = slugify(self.title)  # Generate slug from title
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"