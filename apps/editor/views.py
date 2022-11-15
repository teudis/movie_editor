from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.editor.models import VideoProject, Track
from apps.editor.serializers import VideoProjectSerializer, TrackSerializer, VideoProjectDetailSerializer, \
    TrackDetailsSerializer
from apps.users.authentication import ExternTokenAuthentication


class VideoProjectViewSet(ModelViewSet):
    queryset = VideoProject.objects.all()
    serializer_class = VideoProjectSerializer
    filterset_fields = ['organization_uuid', 'status', ]

    permission_classes = (IsAuthenticated,)
    authentication_classes = (ExternTokenAuthentication, )

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return VideoProjectDetailSerializer
        return self.serializer_class


class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filterset_fields = ['project__id', ]

    permission_classes = (IsAuthenticated,)
    authentication_classes = (ExternTokenAuthentication, )

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TrackDetailsSerializer
        return self.serializer_class
