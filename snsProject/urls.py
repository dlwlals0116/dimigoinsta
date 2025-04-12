from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from articleapp.views import ArticleListView
from snsProject import settings


urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribes/', include('subscribeapp.urls')),
    path('follows/', include('followapp.urls')),
    path('searchs/', include('searchapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
