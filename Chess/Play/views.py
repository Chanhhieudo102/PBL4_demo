from django.shortcuts import render

def play(request):
    return render(request, 'play/play.html')
