from django.shortcuts import render


# Create your views here.
def setsession(request):
    request.session['name'] = 'ravi'
    return render(request, 'student/setsession.html')


def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='Guest')
    keys = request.session.keys()
    items = request.session.items()
    return render(request, 'student/getsession.html',
     {'name':name, 'keys':keys, 'items':items})

def delsession(request):
    if 'name' in request.session:
        request.session.flush()
    return render(request, 'student/delsession.html')