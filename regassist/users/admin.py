from django.contrib import admin
from users.models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('fio',)
    list_display_links = ('fio',)
    search_fields = ('fio',)


admin.site.register(CustomUser, CustomUserAdmin)
