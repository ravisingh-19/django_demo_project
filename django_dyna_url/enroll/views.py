from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'enroll/home.html')

def show(request, my_id):
    return render(request, 'enroll/index.html', {'id':my_id})