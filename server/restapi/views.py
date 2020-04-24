from django.shortcuts import render
from rest_framework import viewsets
from .models import Blogger
from .serializer import BloggerSerializer

# ViewSets define the view behavior.
class BloggerViewSet(viewsets.ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
