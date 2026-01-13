from rest_framework import serializers
from .models import Location, Department, JobOpening, JobDetail,ContactMessage,JobApplication


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


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = [
            "id",
            "job",
            "full_name",
            "email",
            "phone_number",
            "resume",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_resume(self, file):
        allowed_types = ["application/pdf", "application/msword",
                         "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
        if file.content_type not in allowed_types:
            raise serializers.ValidationError("Only PDF or Word documents are allowed.")
        if file.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Resume size must be under 2MB.")
        return file