from django.contrib import admin

from .models import NetworkCredential, Profile

admin.site.register(NetworkCredential)
admin.site.register(Profile)
