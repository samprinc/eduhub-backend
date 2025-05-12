from rest_framework import serializers
from .models import MathLesson, Quiz, QuizQuestion

class MathLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MathLesson
        fields = ['id', 'title',  'video_url', 'form_level','notes_pdf']

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['id', 'question', 'option_a', 'option_b', 'option_c', 'option_d']
