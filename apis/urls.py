from django.urls import path

from .views import PostAPIView, PostDetails

urlpatterns = [
    path("", PostAPIView.as_view(), name="api_post_list"),
    path("post/<int:pk>/", PostDetails.as_view(), name="api_post_detail"),
    
]