# from django.contrib.sitemaps
from random import sample
from string import ascii_letters

from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, status
from rest_framework.response import Response

from .models import URLShort
from .serializers import URLShortSerializer

class CreateShortURLView(generics.GenericAPIView):
    serializer_class = URLShortSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data, context=request)
        serializer.is_valid(raise_exception=True)
        letters = ascii_letters
        long_url = request.data['long_url']
        rand = ''.join(sample(letters, 6))
        current_site = get_current_site(request).domain
        print(current_site)
        short_url = f'http://{current_site}/{rand}'
        serializer.save(long_url=long_url, short_url=short_url)
        return Response(serializer.data)


class RedirectView(generics.GenericAPIView):

    def get(self, request, short_url):
        try:
            current_site = get_current_site(request).domain
            short_url = f'http://{current_site}/{short_url}'
            print(short_url)
            _link = URLShort.objects.get(short_url=short_url)
        except URLShort.DoesNotExist:
            _link = None
        if _link is not None:
            return redirect(to=_link.long_url)
        
        return redirect(to=_link.long_url)