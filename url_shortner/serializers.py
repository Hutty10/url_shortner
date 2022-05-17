from random import sample
from string import ascii_letters

from rest_framework import serializers

from .models import URLShort

class URLShortSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(max_length=10, read_only=True)
    
    class Meta:
        model = URLShort
        fields = '__all__'
