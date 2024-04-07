from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

#test code below to style form video #5
class PostForm(forms.ModelForm):
    class Meta: 
        model = Post 
        fields = (
            'title',
            'content',
            'author',   #this line can be commented out if only superuser is author? 
            'excerpt',
            'featured_image',
            'status',
            'category',
            #'created_on',
            #'updated_on'
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}), # can be commented out if only superuser is author? 
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # test, File input for image

            #'created-on': forms.TextInput(attrs={'class': 'form-control'}),
            #'updated-on': forms.TextInput(attrs={'class': 'form-control'}),
           
        }

#end of test code to style form