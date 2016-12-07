from django.contrib import admin
from .models import WarnedUser


class WarnedUserAdmin(admin.ModelAdmin):
    '''Django admin panel representation of WarnedUser model'''
    list_display = ['user_id', 'warning_count']
    list_filter = ['warning_count']
    search_fields = ['user_id']

    class Meta:
        model = WarnedUser


admin.site.register(WarnedUser, WarnedUserAdmin)
