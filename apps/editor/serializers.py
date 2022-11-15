from rest_framework.serializers import ModelSerializer

from apps.editor.models import VideoProject, Track
from apps.users.serializers import InteractionUserSerializer


class VideoProjectSerializer(ModelSerializer):

    def create(self, validated_data):
        created_by = self.context.get('request').user.interactionuser
        last_modified_by = created_by

        instance = VideoProject.objects.create(
            created_by=created_by,
            last_modified_by=last_modified_by,
            **validated_data
        )
        return instance

    def update(self, instance, validated_data):
        last_modified_by = self.context.get('request').user.interactionuser
        validated_data['last_modified_by'] = last_modified_by
        return super().update(instance, validated_data)

    class Meta:
        model = VideoProject
        fields = "__all__"
        extra_kwargs = {
            'created_by': {'read_only': True},
            'created_date': {'read_only': True},
            'last_modified_by': {'read_only': True},
            'last_modified_date': {'read_only': True},
        }


class VideoProjectDetailSerializer(VideoProjectSerializer):
    created_by = InteractionUserSerializer(read_only=True)
    last_modified_by = InteractionUserSerializer(read_only=True)


class TrackSerializer(ModelSerializer):

    class Meta:
        model = Track
        fields = "__all__"
        extra_kwargs = {
            'created_by': {'read_only': True},
            'created_date': {'read_only': True},
            'last_modified_by': {'read_only': True},
            'last_modified_date': {'read_only': True},
        }

    def create(self, validated_data):
        created_by = self.context.get('request').user.interactionuser
        last_modified_by = created_by

        instance = Track.objects.create(
            created_by=created_by,
            last_modified_by=last_modified_by,
            **validated_data
        )
        return instance

    def update(self, instance, validated_data):
        last_modified_by = self.context.get('request').user.interactionuser
        validated_data['last_modified_by'] = last_modified_by
        return super().update(instance, validated_data)


class TrackDetailsSerializer(TrackSerializer):
    created_by = InteractionUserSerializer(read_only=True)
    last_modified_by = InteractionUserSerializer(read_only=True)
