from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.editor.models import VideoProject, Track
from apps.users.serializers import UserProfileSerializer


class VideoProjectSerializer(ModelSerializer):
    created_by = UserProfileSerializer(read_only=True)
    last_modified_by = UserProfileSerializer(read_only=True)

    class Meta:
        model = VideoProject
        fields = '__all__'
        # fields = ('title', 'organization_uuid', 'status', )
        read_only_fields = ('created_by', 'last_modified_by', )
        extra_kwargs = {
            'organization_uuid': {'read_only': True},
            'status': {'read_only': True},
            'created_by': {'read_only': True},
            'created_date': {'read_only': True},
            'last_modified_by': {'read_only': True},
            'last_modified_date': {'read_only': True},
        }

    def create(self, organization_uuid, validated_data):
        created_by = self.context.get('request').user.userprofile
        last_modified_by = created_by

        instance = VideoProject.objects.create(
            organization_uuid=organization_uuid,
            created_by=created_by,
            last_modified_by=last_modified_by,
            **validated_data
        )
        return instance

    def update(self, instance, validated_data):
        last_modified_by = self.context.get('request').user.userprofile
        validated_data['last_modified_by'] = last_modified_by
        return super().update(instance, validated_data)


class TrackSerializer(ModelSerializer):
    created_by = UserProfileSerializer(read_only=True)
    last_modified_by = UserProfileSerializer(read_only=True)

    class Meta:
        model = Track
        fields = "__all__"
        extra_kwargs = {
            'project': {'read_only': True},
            'created_by': {'read_only': True},
            'created_date': {'read_only': True},
            'last_modified_by': {'read_only': True},
            'last_modified_date': {'read_only': True},
        }

    def create(self, project, validated_data):
        created_by = self.context.get('request').user.userprofile
        last_modified_by = created_by

        instance = Track.objects.create(
            created_by=created_by,
            last_modified_by=last_modified_by,
            project=project,
            **validated_data
        )
        return instance

    # def validate_position(self, value):
    #     print(value)
    #     raise ValidationError('Wrong position')

    def update(self, instance, validated_data):
        last_modified_by = self.context.get('request').user.userprofile
        validated_data['last_modified_by'] = last_modified_by
        return super().update(instance, validated_data)


