from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Collection)
admin.site.register(Message)
admin.site.register(Part)
admin.site.register(Tag)
