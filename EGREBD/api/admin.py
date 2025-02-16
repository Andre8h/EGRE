from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Reader

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (none,{
                'classes': ('wide',),
                'fields': ('username')
            }
        ),
    )

admin.site.register(Reader,CustomUserAdmin)
