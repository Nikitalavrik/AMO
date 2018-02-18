from django.shortcuts import render



def homepage(request):

    """Return start page"""

    
    return render(request, "index.html")