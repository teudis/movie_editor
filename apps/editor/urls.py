from django.urls import path, include
from rest_framework import routers
from apps.editor import views

app_name = 'editor'

project_router = routers.DefaultRouter()
project_router.register('project', views.VideoProjectViewSet, basename="project")

track_router = routers.DefaultRouter()
track_router.register('track', views.TrackViewSet, basename="track")

urlpatterns = [
    path('<uuid:organization_uuid>/', include(project_router.urls)),
    path('<uuid:organization_uuid>/<int:project_id>/', include(track_router.urls)),
]