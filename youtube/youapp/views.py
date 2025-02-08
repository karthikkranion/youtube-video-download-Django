from django.shortcuts import render, redirect
from django.http import HttpResponse
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        
        if not link:
            return HttpResponse("No URL provided.")
        
        try:
            video = YouTube(link)
            stream = video.streams.get_lowest_resolution()
            stream.download()
            return HttpResponse(f"Video '{video.title}' downloaded successfully!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

    return render(request, 'youapp/youtube.html')
