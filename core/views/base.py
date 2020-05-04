from django.shortcuts import render
from django.views.generic import DeleteView as DjangoDeleteView

from ..models import Project
from ..shortcuts import redirect


class DeletionMixin:
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)


class DeleteView(DjangoDeleteView, DeletionMixin):
    pass


def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})
