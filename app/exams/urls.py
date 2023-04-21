from rest_framework.routers import DefaultRouter
from app.exams.views import exams_views

app_name = "exams"

router = DefaultRouter()
router.register(
    "exams",
    exams_views.ExamViewSet,
    basename="exams"
)
router.register("student_exams", exams_views.StudentExamsViewSet, basename="student_exams")
router.register(
    "ordinary_question_user_answers",
    exams_views.OrdinaryQuestionUserAnswerViewSet,
    basename="ordinary_question_user_answers"
)
router.register(
    "comparison_question_user_answers",
    exams_views.ComparisonQuestionUserAnswerViewSet,
    basename="comparison_question_user_answers"
)
router.register(
    "original_question_user_answers",
    exams_views.OriginalQuestionUserAnswerViewSet,
    basename="original_question_user_answers"
)

urlpatterns = router.get_urls()
