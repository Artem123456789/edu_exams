from libs.randomize import get_random_string


def file_ordinary_question_upload(instance, filename):
    y = get_random_string(25)
    extension = filename.split(".")[-1]
    return f"questions/ordinary_question_images/{instance.question.uuid}/{y}.{extension}"


def file_comparison_question_upload(instance, filename):
    y = get_random_string(25)
    extension = filename.split(".")[-1]
    return f"questions/comparison_question_images/{instance.question.uuid}/{y}.{extension}"
