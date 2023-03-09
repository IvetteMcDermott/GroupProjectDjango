from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect
from .forms import AddSpice, SearchCategory
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
        bookmarked = False
        if post.bookmark.filter(id=self.request.user.id).exists():
            bookmarked = True
        comments = post.comments.filter.order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=True)
            comment.post = post
            comment_form = CommentForm()
            comment.save()

        return render(
            request,
            "spice_detail.html",
            {
                "post": post,
                "bookmarked": bookmarked,
                "comments": comments,
                "comment_form": comment_form,
            },
        )


# Bookmark a spice post
class Bookmark(View):

    def post(self, request, slug):
        # gets relevant post
        post = get_object_or_404(Spice, slug=slug)
        if post.bookmark.filter(id=request.user.id).exists():
            post.bookmark.remove(request.user)
        else:
            post.bookmark.add(request.user)

        return HttpResponseRedirect(reverse('spice_detail', args=[slug]))


class AddSpice(CreateView):
    model = Spice
    form_class = AddSpice
    template_name = 'addform.html'
    success_url = '/'
    success_message = 'You got it'


def Search(request):
    model = Spice

    if 'search' in request.POST:
        search = request.POST.get('search')
        search_data = Spice.objects.all()
        search_result = search_data.filter(use_category=search)
        template = 'search.html'

        context = {
            'search': search,
            'object_list': search_result,
        }

        return render(request, template, context)


# class Search(ListView):
#     model = Spice
#     template_name = 'search.html'

#     def get_queryset(self):
#         search = self.request.GET.get('search')
#         search_result = Spice.objects.all().filter(self.use_category == search)
#         print(search_result)
#         print(search)
#         return search_result
