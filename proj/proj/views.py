from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")

from django.shortcuts import render
 
def test(request):
    context = {}
    context['result'] = 'Hello'
    return render(request, 'test.html', context)