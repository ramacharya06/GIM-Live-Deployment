from django.contrib import admin
from .models import Vote
from .models import IPs
# Register your models here.

admin.site.register(Vote)
admin.site.register(IPs)
