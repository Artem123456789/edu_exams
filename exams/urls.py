from rest_framework.routers import DefaultRouter
from exams.views import exams_views

app_name = "exams"

router = DefaultRouter()
router.register("student_exams", exams_views.StudentExamsViewSet, basename="student_exams")
router.register(
    "ordinary_question_user_answers",
    exams_views.OrdinaryQuestionUserAnswerViewSet,
    basename="ordinary_question_user_answers"
)
router.register(
    "exams",
    exams_views.ExamViewSet,
    basename="exams"
)

urlpatterns = router.get_urls()
