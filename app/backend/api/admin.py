from django.contrib import admin
from .models import Project, ProjectFile, DataAnalysis


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'folder_name', 'status', 'created_date', 'modified_date')
    list_filter = ('status', 'created_date')
    search_fields = ('project_name', 'description')
    readonly_fields = ('created_date', 'modified_date')


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'project', 'file_type', 'uploaded_at')
    list_filter = ('file_type', 'uploaded_at')
    search_fields = ('file_name',)
    readonly_fields = ('uploaded_at',)


@admin.register(DataAnalysis)
class DataAnalysisAdmin(admin.ModelAdmin):
    list_display = ('project', 'analysis_type', 'status', 'created_at', 'completed_at')
    list_filter = ('status', 'analysis_type', 'created_at')
    search_fields = ('project__project_name',)
    readonly_fields = ('created_at', 'completed_at')