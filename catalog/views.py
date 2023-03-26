from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import generic

from catalog.models import Newspaper, Redactor, Topic


def index(request):
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()

    context = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
    }
    return render(request, "catalog/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    template_name = "catalog/topic_list.html"
    queryset = Topic.objects.all()
    paginate_by = 3


class NewspaperListView(generic.ListView):
    model = Newspaper
    template_name = "catalog/newspaper_list.html"
    queryset = Newspaper.objects.all()
    paginate_by = 3


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class RedactorListView(generic.ListView):
    model = Redactor
    template_name = "catalog/redactor_list.html"
    queryset = Redactor.objects.all()
    paginate_by = 3



