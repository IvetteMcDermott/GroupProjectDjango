from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import CreateView, ListView
from .forms import AddSpice
from .models import Spice, TypeCategory


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


class SpiceDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Spice.objects.all()
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "spice_detail.html",
            {
                "post": post,
            },
        )


class AddSpice(CreateView):
    model = Spice
    form_class = AddSpice
    template_name = 'addform.html'
    success_url = '/'
    success_message = 'You got it'