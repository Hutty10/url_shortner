from django.urls import path

from .views import CreateShortURLView, RedirectView


urlpatterns = [
    path('', CreateShortURLView.as_view(), name='make_short'),
    path('<str:short_url>', RedirectView.as_view(), name='redirect'),
]
