from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from web.models import Question

def index(request):
    return render(
        request, 
        '/code/web/templates/index.html',
        {
            'questions': Question.objects.all()
        }
    )

def process(request):
    new_question = Question(
        name=request.POST.get("name", ""),
        email=request.POST.get("email", ""),
        topic=request.POST.get("topic", ""),
        text=request.POST.get("text", "")
    )
    new_question.save()
    print(Question.objects.all(), flush=True)
    return redirect('/')
