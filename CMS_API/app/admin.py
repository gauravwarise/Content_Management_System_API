from django.contrib import admin

# Register your models here.
from .models import User, ContentItem
admin.site.register(User)
admin.site.register(ContentItem)