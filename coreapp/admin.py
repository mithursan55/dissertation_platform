from django.contrib import admin
from .models import User, Student, Project, Assignment, MarkingSheet, ModuleLeader

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Assignment)
admin.site.register(MarkingSheet)
admin.site.register(ModuleLeader)
