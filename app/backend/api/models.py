from django.db import models
from django.contrib.auth.models import User
import uuid


class Project(models.Model):
    """プロジェクトモデル"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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


class TableDisplaySettings(models.Model):
    """表表示設定モデル"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_folder = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    
    # 表設定
    table_config = models.JSONField(default=dict)
    
    # グラフ設定
    chart_config = models.JSONField(default=dict)
    
    # レイアウト設定
    layout_config = models.JSONField(default=dict)
    
    # 列メタデータ
    column_metadata = models.JSONField(default=dict)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['project_folder', 'file_name']
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"{self.project_folder}/{self.file_name} - 表示設定"