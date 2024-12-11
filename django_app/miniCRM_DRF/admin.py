from django.contrib import admin
from django.contrib.auth.models import User

from .models import Contact, Deal, Stage, Funnel

admin.site.register(Contact)
admin.site.register(Deal)
admin.site.register(Stage)
admin.site.register(Funnel)