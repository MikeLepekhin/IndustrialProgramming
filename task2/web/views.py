from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from web.models import Question
from web.models import Answer

class QuestionWithAnswers:
    def __init__(self, question, answers):
        self.id = question.id
        self.name = question.name
        self.topic = question.topic
        self.text = question.text
        self.answers = answers
        

def index(request):
    raw_questions = Question.objects.all()
    questions = []
    for question in raw_questions:
        questions.append(QuestionWithAnswers(question, Answer.objects.filter(question_id=question.id)))
    
    return render(
        request, 
        '/code/web/templates/index.html',
        {
            'questions': questions
        }
    )

def process_question(request):
    new_question = Question(
        name=request.POST.get("name", ""),
        email=request.POST.get("email", ""),
        topic=request.POST.get("topic", ""),
        text=request.POST.get("text", "")
    )
    new_question.save()
    print(Question.objects.all(), flush=True)
    return redirect('/')

def process_answer(request):
    new_answer = Answer(
        question_id=request.POST.get("question_id", 1),
        text=request.POST.get("text", "")
    )
    new_answer.save()
    print(Answer.objects.all(), flush=True)
    return redirect('/')
