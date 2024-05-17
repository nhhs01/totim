from django.contrib import admin
from .models import Student, SHobby, Mentor

# Register your models here.
admin.site.register(Mentor)
admin.site.register(SHobby)
admin.site.register(Student)