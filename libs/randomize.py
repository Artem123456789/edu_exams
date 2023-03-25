import random
import string
from string import ascii_lowercase, digits


def get_random_string(length):
    y = "".join(random.choice(ascii_lowercase + digits) for _ in range(length))
    return y

def generate_sms_code(length=5):
    chars = string.digits
    return "".join(random.choice(chars) for _ in range(length))
