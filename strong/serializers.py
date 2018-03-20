from strong.models import Project, Images
from rest_framework import serializers

class ImagesSerializers(serializers.HyperlinkedModelSerializer):
    # description = serializers.StringRelatedField(many=True)
    project_id = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(),source='project.id')
    class Meta:
        model = Images
        fields = ('project_id', 'image')
        # fields = "__all__"
    
    def create(self, validated_data):
        subject = Images.objects.create(parent=validated_data['project']['id'], child_name=validated_data['image'])

        return child

class ProjectSerializers(serializers.ModelSerializer):
    # images = serializers.RelatedField(many=True, queryset=Images.objects.all())
    images = ImagesSerializers(many=True, read_only=True)
    # print(Images.objects.all())
    class Meta:
        model = Project
        fields = ('id', 'type_of_project', 'description', 'images')
        # fields = "__all__"

