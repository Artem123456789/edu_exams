from app.libs.randomize import get_random_string


def file_ordinary_question_upload(instance, filename):
    y = get_random_string(25)
    extension = filename.split(".")[-1]
    return f"questions/ordinary_question_images/{instance.question.uuid}/{y}.{extension}"


def file_comparison_question_upload(instance, filename):
    y = get_random_string(25)
    extension = filename.split(".")[-1]
    return f"questions/comparison_question_images/{instance.question.uuid}/{y}.{extension}"


def file_ordinary_answer_upload(instance, filename):
    y = get_random_string(25)
    extension = filename.split(".")[-1]
    return f"answers/ordinary_answers_files/{instance.answer.uuid}/{y}.{extension}"


def file_comparison_option_upload(instance, filename):
    y = get_random_string(25)
    extension = filename.split(".")[-1]
    return f"answers/comparison_option_files/{instance.option.uuid}/{y}.{extension}"


def file_comparison_option_answer_upload(instance, filename):
    y = get_random_string(25)
    extension = filename.split(".")[-1]
    return f"answers/comparison_option_answer_files/{instance.option_answer.uuid}/{y}.{extension}"
