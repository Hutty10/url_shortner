from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class URLShort(models.Model):
    # owner = models.ForeignKey(User, verbose_name=_("Owner"), on_delete=models.CASCADE)
    # name = models.CharField(_("Short Url Name"), max_length=15, blank=True)
    long_url = models.URLField(_("Long Url"), max_length=999)
    short_url = models.CharField(_("Short Url"), max_length=10, unique=True, blank=True)
    created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Date Updated"), auto_now=True)

    class Meta:
        verbose_name = 'Url Shortner'
        verbose_name_plural = 'Url Shortner'
        ordering = ('-updated',)

    def __str__(self):
        return self.short_url