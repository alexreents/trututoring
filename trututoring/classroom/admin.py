from django.contrib import admin
from django.contrib.auth.admin import Group
from classroom.models import User

admin.site.unregister(Group)
admin.site.register(User)

admin.site.site_header = 'TRU Tutoring Admin'