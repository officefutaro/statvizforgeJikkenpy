from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FileViewSet, DataViewSet, server_info

router = DefaultRouter()
router.register(r'files', FileViewSet, basename='file')
router.register(r'data', DataViewSet, basename='data')

urlpatterns = [
    path('', include(router.urls)),
    path('projects/list', ProjectViewSet.as_view({'get': 'list'}), name='project-list'),
    path('projects/create', ProjectViewSet.as_view({'post': 'create'}), name='project-create'),
    path('projects/<int:pk>/', ProjectViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='project-detail'),
    path('server-info/', server_info, name='server_info'),
]