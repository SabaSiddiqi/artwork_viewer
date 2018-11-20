from django.shortcuts import render, render_to_response


def homepage(request):
    template = 'artview/home.html'
    return render_to_response(template)

def mainpage(request):
    template = 'artview/slider.html'
    return render_to_response(template)
