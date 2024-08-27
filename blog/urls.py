from . import views
from django.urls import path
from .views import (
    AddPostView, LikeView, UpdatePostView, DeletePostView,
    AddCategoryView, CategoryView, CategoryListView
)

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_new_post/', AddPostView.as_view(), name='add_new_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('like/<slug:slug>', LikeView, name='like_post'),
    path('post/edit/<slug:slug>', UpdatePostView.as_view(
        ), name='update_post'),
    path('post/<slug:slug>/remove', DeletePostView.as_view(
        ), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
]
