from django.contrib import admin
from django.contrib.auth.admin import Group
from classroom.models import User, Subject, Grade, Availability, Session, Student, Teacher

admin.site.unregister(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Availability)
admin.site.register(Session)

admin.site.site_header = 'TRU Tutoring Admin'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'  # Users ordered from newest to oldest

    fields = ('first_name', 'last_name', ('is_student', 'is_teacher'), 'username', 'password', 'email', 'is_active', ('date_joined', 'last_login'), ('is_superuser', 'is_staff')) 
