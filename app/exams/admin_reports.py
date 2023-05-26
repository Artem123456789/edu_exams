from typing import List

import pandas as pd

from app.exams.handlers.exams_handlers import StudentExamsHandler
from app.exams.models import Exam, StudentExam


def exam_report(queryset) -> pd.DataFrame:
    data: List[Exam] = list(queryset)
    exam = data[0]
    student_exams = StudentExam.objects.filter(exam=exam)
    results = []
    for student_exam in student_exams:
        result = StudentExamsHandler().get_student_exam_results(student_exam=student_exam)
        results.append(
            {
                "user_name": student_exam.user_name,
                "points": result.points,
                "hours_pass": result.hours_pass,
                "minutes_pass": result.minutes_pass,
                "seconds_pass": result.seconds_pass
            }
        )

    dictionary = {}
    fields = [
        "user_name",
        "points",
        "hours_pass",
        "minutes_pass",
        "seconds_pass",
    ]
    for row in results:
        for field in fields:
            attr = row[field]
            tmp_arr = dictionary.get(field, [])
            tmp_arr.append(attr)
            dictionary[field] = tmp_arr

    return pd.DataFrame(dictionary)
