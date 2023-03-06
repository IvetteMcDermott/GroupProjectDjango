from django.shortcuts import render

# Create your views here.


def index(request):
    """ RENDER INDEX/LANDING PAGE  """
    return render(request, 'index.html')
