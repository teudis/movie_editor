from rest_framework import routers
from apps.editor import views

app_name = 'editor'

router = routers.DefaultRouter()
router.register('project', views.VideoProjectViewSet, basename="project")
router.register('track', views.TrackViewSet, basename="track")

urlpatterns = router.urls
