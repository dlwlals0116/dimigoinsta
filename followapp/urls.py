from django.urls import path
from followapp.views import FollowView, FollowListView


app_name = "followapp"


urlpatterns = [
    path('follow/', FollowView.as_view(), name='follow'),
    path('list/', FollowListView.as_view(), name='list'),
]
