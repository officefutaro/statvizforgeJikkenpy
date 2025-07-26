from rest_framework import serializers
from .models import Project, ProjectFile, DataAnalysis


class ProjectSerializer(serializers.ModelSerializer):
    """プロジェクトシリアライザー"""
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'modified_date')


class ProjectFileSerializer(serializers.ModelSerializer):
    """プロジェクトファイルシリアライザー"""
    class Meta:
        model = ProjectFile
        fields = '__all__'
        read_only_fields = ('id', 'uploaded_at',)


class DataAnalysisSerializer(serializers.ModelSerializer):
    """データ分析シリアライザー"""
    class Meta:
        model = DataAnalysis
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'completed_at')