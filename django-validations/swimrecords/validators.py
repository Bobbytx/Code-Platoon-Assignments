
from django.core.exceptions import ValidationError

def validate_stroke(stroke):
    valid_strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle', 'relay']
    if stroke not in valid_strokes:
        raise ValidationError(f"{stroke} is not a valid stroke")

def validate_distance(distance):
    if distance < 50:
        raise ValidationError(f"{distance} is not a valid distance")