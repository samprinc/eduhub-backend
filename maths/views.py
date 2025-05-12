from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MathLesson, Quiz, QuizQuestion
from .serializers import MathLessonSerializer, QuizQuestionSerializer
from django.shortcuts import render
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def lesson_list_api(request):
    if request.method == 'GET':
        lessons = MathLesson.objects.all()
        serializer = MathLessonSerializer(lessons, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MathLessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
from django.http import Http404
from rest_framework import status
@api_view(['GET'])
def quiz_questions_api(request, lesson_id):
    try:
        quiz = Quiz.objects.get(lesson_id=lesson_id)
        questions = QuizQuestion.objects.filter(quiz=quiz)
        serializer = QuizQuestionSerializer(questions, many=True)
        return Response({
            "quiz_title": quiz.title,
            "questions": serializer.data
        })
    except Quiz.DoesNotExist:
        return Response({"error": "Quiz not found"}, status=404)



def student_dashboard(request):
    return render(request, 'student_dashboard.html')
