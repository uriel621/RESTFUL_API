from strong.models import Project, Images
from rest_framework import serializers

class ImagesSerializers(serializers.HyperlinkedModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(),source='project.id')
    class Meta:
        model = Images
        fields = ('project_id', 'image')

    def create(self, validated_data):
        subject = Images.objects.create(parent=validated_data['project']['id'], child_name=validated_data['image'])
        return child

class ProjectSerializers(serializers.ModelSerializer):
    images = ImagesSerializers(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('type_of_project', 'description', 'images')
        # fields = "__all__"

