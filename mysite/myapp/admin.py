
from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import AllowedIP

# Register the AllowedIP model with the admin site
admin.site.register(AllowedIP)

admin.site.register(Permission)