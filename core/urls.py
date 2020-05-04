from django.urls import path

from . import views
from . import url_names

urlpatterns = [
    path("", views.home, name=url_names.home),
    path("projects/<int:pk>/", views.ProjectView.as_view(), name=url_names.project),
    path(
        "projects/create/",
        views.ProjectCreateView.as_view(),
        name=url_names.project_create,
    ),
    path(
        "projects/update/<int:pk>/",
        views.ProjectUpdateView.as_view(),
        name=url_names.project_update,
    ),
    path(
        "projects/delete/<int:pk>/",
        views.ProjectDeleteView.as_view(),
        name=url_names.project_delete,
    ),
    path("projects/<int:pk>/messages/", views.MessagesView.as_view(), name=url_names.messages),
    path(
        "projects/<int:pk>/messages/create/",
        views.MessageCreateView.as_view(),
        name=url_names.message_create,
    ),
    path("messages/<int:pk>/", views.MessageView.as_view(), name=url_names.message),
    path(
        "messages/<int:pk>/update/",
        views.MessageUpdateView.as_view(),
        name=url_names.message_update,
    ),
    path(
        "messages/<int:pk>/delete/",
        views.MessageDeleteView.as_view(),
        name=url_names.message_delete,
    ),
]
