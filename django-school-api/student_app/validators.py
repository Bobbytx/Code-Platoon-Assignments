import re
from django.core.exceptions import ValidationError

def validate_name_format(name):
    error_message='Name must be in the format "First Middle Initial. Last"'
    regex = re.compile(r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$')
    good_name = re.match(regex, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={ 'name' : name })


def validate_school_email(student_email):
    error_message='Invalid school email format. Please use an email ending with "@school.com".'
    regex = re.compile(r'^.+@school\.com$')
    good_email = re.match(regex, student_email)
    if good_email:
        return student_email
    else:
        raise ValidationError(error_message, params={ 'student_email' : student_email})

def validate_combination_format(combo):
    error_message='Combination must be in the format "12-12-12"'
    regex = re.compile(r'^\d{2}-\d{2}-\d{2}$')
    good_combo = re.match(regex, combo)
    if good_combo:
        return combo
    else:
        raise ValidationError(error_message, params={ 'combo' : combo })