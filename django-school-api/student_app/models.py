from django.db import models
from django.core import validators as v
from .validators import validate_name_format, validate_school_email, validate_combination_format

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null=False, validators=[validate_name_format])
    student_email = models.EmailField(max_length=255, null=False, unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(max_length=255, null=True, unique=False)
    locker_number = models.PositiveIntegerField(null=False, unique=True, default=110, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(null=False, default='12-12-12', validators=[validate_combination_format])
    good_student = models.BooleanField(null=False, default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def reassign_locker(self, new_locker_number):
        self.locker_number = new_locker_number
        self.save()

    def student_status(self, bool):
        self.good_student = bool
        self.save()