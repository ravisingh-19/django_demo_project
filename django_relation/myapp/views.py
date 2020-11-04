from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')
    
def show_user_data(request):
    return render(request, 'myapp/user.html')

def show_page_data(request):
    return render(request, 'myapp/page.html')

def show_song_data(request):
    return render(request, 'myapp/song.html')

def show_post_data(request):
    return render(request, 'myapp/post.html')