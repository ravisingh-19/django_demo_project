from django.shortcuts import render

# Create your views here.

def learn_django(request):
    return render(request, 'course/courseone.html', {'name': 'ML'})

def learn_python(request):
    return render(request, 'course/coursetwo.html')