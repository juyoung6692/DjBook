#blog/urls.py
from django.urls import path, re_path
from blog import views

app_name='blog'
urlpatterns = [
    path('',views.PostLV.as_view(), name='index'),

    #same as /blog/
    path('post/', views.PostLV.as_view(), name='post_list'),

    #한글이 포함된 슬러그 처리, path('post/<slug:slug>로 하면 한글이 포함된 슬러그는 처리하지 못함
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/',views.TaggedObjectLV.as_view(), name='tagged_object_list'),

    path('add/', views.PostCreateView.as_view(), name="add"),
    path('change/', views.PostChangeLV.as_view(), name="change"),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete"),
]