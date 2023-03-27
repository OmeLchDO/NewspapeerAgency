from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import generic

from catalog.models import Newspaper, Redactor, Topic


def index(request):
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_visits": num_visits + 1
    }
    return render(request, "catalog/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    template_name = "catalog/topic_list.html"
    queryset = Topic.objects.all()
    paginate_by = 3


class TopicDetailView(generic.DetailView):
    model = Topic


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


class RedactorDetailView(generic.DetailView):
    model = Redactor
