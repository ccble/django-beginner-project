from django.shortcuts import render

from rest_framework import generics

from blog.models import Post

from .serializers import PostSerializer

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetails (generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Create your views here.
