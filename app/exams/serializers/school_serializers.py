from rest_framework import serializers

from app.exams.handlers.exams_handlers import StudentExamsHandler
from app.exams.models import (
    School,
    Exam,
    StudentExam,
)


class SchoolListSerializer(serializers.ModelSerializer):
    exams_count = serializers.SerializerMethodField()
    performance_rate = serializers.SerializerMethodField()

    def get_exams_count(self, obj: School):
        return Exam.objects.filter(subject__school=obj).count()

    def get_performance_rate(self, obj: School):
        points = 0
        school_exams = Exam.objects.filter(subject__school=obj)
        school_student_exams = StudentExam.objects.filter(exam__in=school_exams)
        for student_exam in school_student_exams:
            points += StudentExamsHandler().get_student_exam_results(student_exam).points

        return points

    class Meta:
        model = School
        fields = [
            'name',
            'exams_count',
            'performance_rate'
        ]
