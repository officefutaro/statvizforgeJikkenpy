from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """プロジェクトモデル"""
    folder_name = models.CharField(max_length=255, unique=True)
    project_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='active')
    tags = models.JSONField(default=list, blank=True)
    
    class Meta:
        ordering = ['-modified_date']
    
    def __str__(self):
        return self.project_name


class ProjectFile(models.Model):
    """プロジェクトファイルモデル"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='project_files/')
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.project.project_name} - {self.file_name}"


class DataAnalysis(models.Model):
    """データ分析モデル"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='analyses')
    analysis_type = models.CharField(max_length=100)
    parameters = models.JSONField(default=dict)
    status = models.CharField(max_length=50, default='pending')
    result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.project.project_name} - {self.analysis_type}"