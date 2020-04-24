from rest_framework import serializers
from .models import Blogger

# Serializers define the API representation.
class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogger
        fields = ['url', 'title', 'body']