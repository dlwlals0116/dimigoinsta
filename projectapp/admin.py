from django.contrib import admin
from projectapp.models import Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project


admin.site.register(Project, ProjectAdmin)