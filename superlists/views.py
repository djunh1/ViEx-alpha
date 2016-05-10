from django.shortcuts import render

'''
Keep views here static e.g serving up an html template as its only function.
'''


def faq(request):
    return render(request, 'faq/faq.html', {})


def toc(request):
    return render(request, 'toc/toc.html', {})


