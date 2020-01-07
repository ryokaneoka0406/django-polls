from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at qestion %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of qestion %s." 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on qestion %s." % question_id)