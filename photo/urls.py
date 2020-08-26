from django.urls import  path
from photo import views

app_name = 'photo'
urlpatterns=[
    #Example:/photo/
    #as_view(model=Photo)같이 작성하면 뷰는 따로 작성하지 않아도됨
    path('', views.AlbumLV.as_view(), name='index'),
    path('album/', views.AlbumLV.as_view(), name='album_list'),
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),
]