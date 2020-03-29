from django.contrib import admin
from django.contrib.auth.admin import Group
from classroom.models import User, Subject

admin.site.unregister(Group)
admin.site.register(Subject)

admin.site.site_header = 'TRU Tutoring Admin'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


