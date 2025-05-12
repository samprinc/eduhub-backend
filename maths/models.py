from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade_level = models.CharField(max_length=20, choices=[
        ('Form 1', 'Form 1'), ('Form 2', 'Form 2'),
        ('Form 3', 'Form 3'), ('Form 4', 'Form 4')
    ])
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username


class MathLesson(models.Model):
    title = models.CharField(max_length=100)
    form_level = models.CharField(max_length=20, choices=[
        ('Form 1', 'Form 1'), ('Form 2', 'Form 2'),
        ('Form 3', 'Form 3'), ('Form 4', 'Form 4')
    ])
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    notes_pdf = models.FileField(upload_to='notes_pdfs/', null=True, blank=True)  # <-- ADD THIS
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.form_level} - {self.title}"


class Quiz(models.Model):
    lesson = models.ForeignKey(MathLesson, related_name="quizzes", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    question = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.question


class StudentScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.quiz} - {self.score}"
