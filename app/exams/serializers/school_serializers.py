from rest_framework import serializers

from app.exams.models import (
    School,
    Exam,
)


class SchoolListSerializer(serializers.ModelSerializer):
    exams_count = serializers.SerializerMethodField()

    def get_exams_count(self, obj: School):
        return Exam.objects.filter(subject__school=obj).count()

    class Meta:
        model = School
        fields = [
            'name',
            'exams_count',
        ]
