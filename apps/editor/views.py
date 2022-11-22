from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.create(organization_uuid=self.kwargs.get('organization_uuid'),
                                    validated_data=request.data,
                                    )
        serializer = self.get_serializer(instance=project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    permission_classes = (IsAuthenticated,)
    authentication_classes = (ExternTokenAuthentication, )

    pagination_class = None


    def get_queryset(self):
        organization_uuid = self.kwargs.get('organization_uuid')
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(VideoProject,
                                    organization_uuid=organization_uuid,
                                    id=project_id,
                                    )
        return project.time_line

    def create(self, request, *args, **kwargs):
        organization_uuid = self.kwargs.get('organization_uuid')
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(VideoProject,
                                    organization_uuid=organization_uuid,
                                    id=project_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        track = serializer.create(project=project,
                                  validated_data=request.data,
                                  )
        serializer = self.get_serializer(instance=track)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
