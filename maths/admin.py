from django.contrib import admin
from .models import Student, MathLesson, Quiz, QuizQuestion, StudentScore

# Register models
admin.site.register(Student)
admin.site.register(MathLesson)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(StudentScore)
