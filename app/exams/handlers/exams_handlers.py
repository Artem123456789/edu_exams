from app.exams.entities.exams_entites import StudentExamResultsOutputEntity
from app.exams.models import (
    StudentExam,
    OrdinaryQuestionUserAnswer,
    ComparisonQuestionUserAnswer,
    OrdinaryQuestion,
    ComparisonQuestionOption,
    OriginalQuestion,
    OriginalQuestionAnswer,
    OriginalQuestionUserAnswer,
    OriginalQuestionBetweenAnswerItem,
    OriginalQuestionBetweenUserAnswer,
    Exam,
    OriginalBetweenQuestion,
    ComparisonQuestion,
)

from datetime import datetime
from django.db.models import Sum


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

    def __get_student_exam_original_questions_points(self, student_exam: StudentExam) -> int:
        original_questions_answers = OriginalQuestionUserAnswer.objects.filter(student_exam=student_exam)
        points = 0

        for user_answer in original_questions_answers:
            question_answer = OriginalQuestionAnswer.objects.get(question=user_answer.question)
            if user_answer.text == question_answer.text:
                points += user_answer.question.right_answer_points

        return points

    def __get_student_exam_original_between_questions_points(self, student_exam: StudentExam) -> int:
        original_between_questions_answers = OriginalQuestionBetweenUserAnswer.objects.filter(student_exam=student_exam)
        points = 0

        for user_answer in original_between_questions_answers:
            if user_answer.text == user_answer.item.text_answer:
                points += user_answer.item.right_answer_points

        return points

    def __get_ordinary_questions_exam_max_points(self, exam: Exam):
        exam_ordinary_questions = OrdinaryQuestion.objects.filter(exam=exam)
        points = exam_ordinary_questions.aggregate(Sum('right_answer_points'))['right_answer_points__sum']
        return points if points else 0

    def __get_original_questions_exam_max_points(self, exam: Exam):
        exam_original_questions = OriginalQuestion.objects.filter(exam=exam)
        points = exam_original_questions.aggregate(Sum('right_answer_points'))['right_answer_points__sum']
        return points if points else 0

    def __get_comparison_questions_exam_max_poins(self, exam: Exam):
        options = ComparisonQuestionOption.objects.filter(question__exam=exam)
        points = options.aggregate(Sum('right_answer_points'))['right_answer_points__sum']
        return points if points else 0

    def __get_original_between_questions_exam_max_points(self, exam: Exam):
        exam_original_between_questions = OriginalQuestionBetweenAnswerItem.objects.filter(question__exam=exam)
        points = exam_original_between_questions.aggregate(Sum('right_answer_points'))['right_answer_points__sum']

        return points if points else 0

    def get_exam_max_points(self, exam: Exam) -> int:
        ordinary_questions_sum = self.__get_ordinary_questions_exam_max_points(exam=exam)
        original_questions_sum = self.__get_original_questions_exam_max_points(exam=exam)
        comparison_questions_sum = self.__get_comparison_questions_exam_max_poins(exam=exam)
        original_between_questions_sum = self.__get_original_between_questions_exam_max_points(exam=exam)

        return ordinary_questions_sum + original_questions_sum + comparison_questions_sum + original_between_questions_sum

    def get_student_exam_pass_time(self, student_exam: StudentExam) -> (int, int, int):
        if student_exam.is_not_finished():
            exam = student_exam.exam
            return exam.hours_to_pass, exam.minutes_to_pass, exam.seconds_to_pass
        else:
            delta = student_exam.end_datetime - student_exam.created
            delta_str = str(delta).split(':')
            return int(delta_str[0]), int(delta_str[1]), int(delta_str[2].split('.')[0])

    def get_student_exam_results(self, student_exam: StudentExam) -> StudentExamResultsOutputEntity:
        points = self.__get_student_exam_ordinary_questions_points(student_exam=student_exam)
        points += self.__get_student_exam_comparison_questions_points(student_exam=student_exam)
        points += self.__get_student_exam_original_questions_points(student_exam=student_exam)
        points += self.__get_student_exam_original_between_questions_points(student_exam=student_exam)

        max_exam_points = self.get_exam_max_points(exam=student_exam.exam)
        hours_pass, minutes_pass, seconds_pass = self.get_student_exam_pass_time(student_exam=student_exam)

        return StudentExamResultsOutputEntity(
            points=points,
            max_points=max_exam_points,
            hours_pass=hours_pass,
            minutes_pass=minutes_pass,
            seconds_pass=seconds_pass,
        )

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
        return ComparisonQuestionUserAnswer.objects.filter(
            student_exam=student_exam,
            option=option,
        ).count() > 0


class OriginalQuestionAnswersHandler:

    @staticmethod
    def is_answered(
            student_exam: StudentExam,
            question: OriginalQuestion,
    ):
        return OriginalQuestionUserAnswer.objects.filter(
            student_exam=student_exam,
            question=question,
        ).count() > 0


class OriginalQuestionBetweenAnswersHandler:

    @staticmethod
    def is_answered(
            student_exam: StudentExam,
            item: OriginalQuestionBetweenAnswerItem,
    ):
        return OriginalQuestionBetweenUserAnswer.objects.filter(
            student_exam=student_exam,
            item=item,
        ).count() > 0
