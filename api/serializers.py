from rest_framework import serializers

from .models import PackageRelease, Project
from .pypi import version_exists, latest_version


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ["name", "version"]
        extra_kwargs = {"version": {"required": False}}

    def validate(self, data):
        name_pack = data.get("name")
        version = data.get("version")
        if version is None:
            data["version"] = latest_version(name_pack)
        
        if version_exists(name_pack, version) is True:
            return data
        else:
            raise serializers.ValidationError({"error": "One or more packages doesn't exist"})


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "packages"]

    packages = PackageSerializer(many=True)

    def create(self, validated_data):
        project = Project.objects.create(name=validated_data.get('name'))
        for package_data in validated_data.get('packages'):
            PackageRelease.objects.create(project=project, **package_data)
        return project
