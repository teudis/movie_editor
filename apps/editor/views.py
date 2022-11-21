from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.editor.models import VideoProject, Track
from apps.editor.serializers import VideoProjectSerializer, TrackSerializer
from apps.users.authentication import ExternTokenAuthentication


class VideoProjectViewSet(ModelViewSet):

    queryset = VideoProject.objects.all()
    serializer_class = VideoProjectSerializer

    filterset_fields = ['status', ]

    permission_classes = (IsAuthenticated,)
    authentication_classes = (ExternTokenAuthentication, )

    def get_queryset(self):
        organization_uuid = self.kwargs.get('organization_uuid')
        queryset = super().get_queryset().filter(organization_uuid=organization_uuid)
        return queryset


class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    permission_classes = (IsAuthenticated,)
    authentication_classes = (ExternTokenAuthentication, )

    def get_queryset(self):
        organization_uuid = self.kwargs.get('organization_uuid')
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(VideoProject,
                                    organization_uuid=organization_uuid,
                                    id=project_id,
                                    )
        return project.time_line
