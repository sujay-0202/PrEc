from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello World Ram ! </h1>')
