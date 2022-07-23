# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    # Get the text
    djtext= request.POST.get('text','default')
    #print(djtext)
    
    # Check checkbox values
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover','off')
    extraspaceremover= request.POST.get('extraspaceremover','off')
    charactercounter= request.POST.get('charactercounter','off')
 
    # Check which checkbox is on 
    if removepunc == "on":
        punctuations= '''!()-[]{};:\,<>./?@#$%^&*'"~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
        
    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        params = {'purpose':'Changed to uppercase','analyzed_text':analyzed}
        
    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'New line removed','analyzed_text':analyzed}
        
    if extraspaceremover == "on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char      
        djtext = analyzed  
        params = {'purpose':'Extra spaces removed ','analyzed_text':analyzed}
        
    if charactercounter == "on":
        counter = 0 
        for char in djtext:
            if char != " ":
                counter = counter + 1
        
        params = {'purpose':'Number of characters is given below','analyzed_text':analyzed,'charcounter':counter}

    return render(request, 'analyze.html', params)    
    