from django.shortcuts import render
from django.views import generic, View
from django.views.generic import CreateView, ListView
from .models import Spice
from .forms import AddSpice


# Create your views here.


def index(request):
    """ RENDER INDEX/LANDING PAGE  """
    return render(request, 'index.html')


class ListSpices(ListView):
    """ RENDER LIST OF ITEMS """
    """ NOTICE WHEN USING CLASS FOR THE VIEW: """
    """ YOU WILL NEED TO CALL IT IN THE FRONT END """
    """ LIKE OBJECT IN OBJECT_LIST A DIFFERENCE THAN FUNCTION BASED """

    model = Spice
    queryset = model.objects.all()
    template_name = 'listview.html'


class AddSpice(CreateView):
    model = Spice
    form_class = AddSpice
    template_name = 'addform.html'
    success_url = '/'
    success_message = 'You got it'