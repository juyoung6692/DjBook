#boomark/urls.py
from django.urls import path
from bookmark import views

#함수 뷰일때는 뷰이름만 쓰면 되지만 클래스형 뷰일때는 as_view()를 붕여줘야 작동함
app_name='bookmark'
urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    #Bookmark add
    path('add/',views.BookmarkCreateView.as_view(), name="add"),
    #change
    path('change/', views.BookmarkChangeLV.as_view(), name="change"),
    #update
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update"),
    #delete
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete"),

]