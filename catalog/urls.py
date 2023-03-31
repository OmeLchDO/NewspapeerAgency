from django.urls import path

from catalog.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"
    ),

    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),

    path(
        "topics/<int:pk>/update",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),

    path(
        "topics/<int:pk>/delete",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),

    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list"
    ),

    path(
        "newspapers/<int:pk>",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),

    path(
        "newspapers/create",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),

    path(
        "newspapers/<int:pk>/update",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),

    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
    ),

    path(
        "redactors/<int:pk>",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),

    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"),
]

app_name = "catalog"
