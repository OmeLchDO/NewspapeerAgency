from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import RedactorCreateForm, NewspaperForm, NewspaperSearchForm
from catalog.models import Newspaper, Redactor, Topic


@login_required
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


def logged_view(request):
    logout(request)
    return render(request, "registration/logged_out.html")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "catalog/topic_list.html"
    queryset = Topic.objects.all()
    paginate_by = 3


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_form.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_form.html"


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "catalog/topic_confirm_delete.html"
    success_url = reverse_lazy("catalog:topic-list")


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "catalog/newspaper_list.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = NewspaperSearchForm(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        queryset = Newspaper.objects.all()

        form = NewspaperSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )

        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "catalog/redactor_list.html"
    queryset = Redactor.objects.all()
    paginate_by = 3


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_form.html"


