#boomark/urls.py
from django.urls import path
from bookmark.views import BookmarkDV, BookmarkLV

#함수 뷰일때는 뷰이름만 쓰면 되지만 클래스형 뷰일때는 as_view()를 붕여줘야 작동함
app_name='bookmark'
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]