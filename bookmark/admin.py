from django.contrib import admin
from bookmark.models import Bookmark

#admin 사이트에서 테이블을 어떤 모습으로 보여줄지 정의

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')