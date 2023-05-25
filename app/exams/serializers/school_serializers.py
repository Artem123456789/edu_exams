from rest_framework import serializers

from app.exams.models import School


class SchoolListSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = [
            'name',
        ]
