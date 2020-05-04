from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from ..forms import MessageForm, ProjectForm
from ..models import Message, Project
from ..shortcuts import redirect
from .. import url_names
from .base import DeleteView


class ProjectView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        return render(request, "projects/project.html", {"project": project})


class ProjectCreateView(View):
    form = ProjectForm
    template_name = "projects/project_create.html"

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect(project)

        return render(request, self.template_name, {"form": form})


class ProjectUpdateView(UpdateView):
    model = Project
    context_object_name = "project"
    form_class = ProjectForm
    template_name = "projects/project_update.html"


class ProjectDeleteView(DeleteView):
    model = Project
    context_object_name = "project"
    template_name = "projects/project_delete.html"
    success_url = reverse_lazy(url_names.home)


class MessagesView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        messages = Message.objects.filter(project=project)
        return render(
            request,
            "projects/messages.html",
            {"messages": messages, "project": project},
        )


LONG_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
SHORT_DATETIME_FORMAT = "%b %-d"


class MessageView(View):
    def get(self, request, pk):
        queryset = Message.objects.select_related("project")
        message = get_object_or_404(queryset, pk=pk)
        edited_at_long = message.edited_at.strftime(LONG_DATETIME_FORMAT)
        edited_at_short = message.edited_at.strftime(SHORT_DATETIME_FORMAT)

        return render(
            request,
            "projects/message.html",
            {
                "message": message,
                "project": message.project,
                "edited_at_long": edited_at_long,
                "edited_at_short": edited_at_short,
            },
        )


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "projects/message_create.html"

    def get_initial(self):
        return {"project": self.kwargs.get("pk")}

    def get_context_data(self):
        context = {}
        context["project"] = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse_lazy(url_names.messages, args=(self.kwargs.get("pk"),))


class MessageUpdateView(UpdateView):
    model = Message
    context_object_name = "message"
    form_class = MessageForm
    template_name = "projects/message_update.html"


class MessageDeleteView(DeleteView):
    model = Message
    context_object_name = "message"
    template_name = "projects/message_delete.html"
    success_url = reverse_lazy(url_names.home)
