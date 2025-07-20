from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FileViewSet, DataViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'files', FileViewSet, basename='file')
router.register(r'data', DataViewSet, basename='data')

urlpatterns = [
    path('', include(router.urls)),
]