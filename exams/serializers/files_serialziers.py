from rest_framework import serializers

from exams.models import (
    OrdinaryQuestionFileModel,
)


class OrdinaryQuestionFileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdinaryQuestionFileModel
        fields = [
            "type",
            "file",
        ]
