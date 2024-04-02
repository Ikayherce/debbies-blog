from . import views
from django.urls import path
from .views import AddPostView, LikeView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_new_post/', AddPostView.as_view(), name='add_new_post'),  #test code for new post view
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('like/<int:pk>', LikeView, name='like_post'),  #test code for like functionality 
    
]