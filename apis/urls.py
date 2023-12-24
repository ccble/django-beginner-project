from django.urls import path

from .views import PostAPIView, PostDetails

urlpatterns = [
    path("", PostAPIView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetails.as_view(), name="post_detail"),
    
]