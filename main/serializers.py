from rest_framework import serializers
from .models import Location, Department, JobOpening, JobDetail,ContactMessage


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name"]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name"]


class JobOpeningSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    function = DepartmentSerializer()

    class Meta:
        model = JobOpening
        fields = [
            "id",
            "title",
            "short_description",
            "location",
            "function",
            "is_active",
            "created_at",
        ]


class JobDetailSerializer(serializers.ModelSerializer):
    job = JobOpeningSerializer()

    class Meta:
        model = JobDetail
        fields = [
            "job",
            "responsibilities",
            "requirements",
            "nice_to_have",
            "experience_required",
        ]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "name",
            "email",
            "subject",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]