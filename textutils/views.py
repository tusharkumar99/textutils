from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    caps = request.POST.get('caps', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    wordcount = request.POST.get('wordcount', 'off')

    p=""
    c="Count not selected"
    s = djtext

    if removepunc == 'on':
        p+="Remove Punctuation"
        s=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                s = s + char

    if caps == 'on':
        p+=" Capitalize"
        s = s.upper()

    if newlinerem == 'on':
        p+=" New Line Remover"
        temp_s = ""
        for char in s:
            if char != "\n" and char != "\r":
                temp_s= temp_s+char
        s=temp_s
    
    if wordcount == 'on':
        p+=" Word Count"
        c=1
        for char in s:
            if char == " " or char == "\n":
                c+=1
        
    params = {
            'purpose' : p,
            'analyzed_text' : s,
            'count':c
            }
   

    if wordcount == 'off' and newlinerem == 'off' and caps == 'off' and removepunc == 'off':
        return render(request, 'error.html', params)

    return render(request, 'analyze.html', params)