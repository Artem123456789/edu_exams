from exams.entities.exams_entites import StudentExamResultsOutputEntity
from exams.models import (
    StudentExam,
    OrdinaryQuestionUserAnswer,
    ComparisonQuestionUserAnswer,
    OrdinaryQuestion,
    ComparisonQuestionOptionAnswer,
    ComparisonQuestionOption,
)

from datetime import datetime


class StudentExamsHandler:

    def __get_student_exam_ordinary_questions_points(self, student_exam: StudentExam) -> int:
        ordinary_questions_answers = OrdinaryQuestionUserAnswer.objects.filter(student_exam=student_exam)
        points = 0

        for user_answer in ordinary_questions_answers:
            if user_answer.answer.is_correct:
                points += user_answer.question.right_answer_points

        return points

    def __get_student_exam_comparison_questions_points(self, student_exam: StudentExam) -> int:
        comparison_questions_answers = ComparisonQuestionUserAnswer.objects.filter(student_exam=student_exam)
        points = 0

        for user_answer in comparison_questions_answers:
            if user_answer.option.option_answer == user_answer.option_answer:
                points += user_answer.option.right_answer_points

        return points

    def get_student_exam_results(self, student_exam: StudentExam) -> StudentExamResultsOutputEntity:
        points = self.__get_student_exam_ordinary_questions_points(student_exam=student_exam)
        points += self.__get_student_exam_comparison_questions_points(student_exam=student_exam)

        return StudentExamResultsOutputEntity(points=points)

    @staticmethod
    def finish_student_exam(student_exam: StudentExam) -> None:
        if student_exam.is_not_finished:
            student_exam.end_datetime = datetime.now()
            student_exam.save()


class OrdinaryQuestionAnswersHandler:

    @staticmethod
    def is_answered(
            student_exam: StudentExam,
            question: OrdinaryQuestion
    ):
        return OrdinaryQuestionUserAnswer.objects.filter(
            student_exam=student_exam,
            question=question,
        ).count() > 0


class ComparisonQuestionAnswersHandler:

    @staticmethod
    def is_question_option_answered(
            student_exam: StudentExam,
            option: ComparisonQuestionOption,
    ):
        return ComparisonQuestionOptionAnswer.objects.filter(
            student_exam=student_exam,
            option=option,
        ).count() > 0
