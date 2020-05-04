from datetime import datetime
import pytz

import pytest
from django.urls import reverse

from ..models import Project, Message
from .. import url_names


@pytest.fixture
def project():
    return Project.objects.create(name="Programming")


## Project Model tests
@pytest.mark.django_db
def test_create_project():
    result = Project.objects.create(name="Programming")
    assert result.name == "Programming"


## Message Model tests
@pytest.mark.django_db
def test_save_datetime_when_save_message(project):
    m = Message(title="Programming", project=project)
    m.full_clean()
    assert m.edited_at is not None


## Project View tests
@pytest.mark.django_db
def test_project_create_view(client):
    response = client.get(reverse(url_names.project_create))
    assert response.status_code == 200


@pytest.mark.django_db
def test_project_create_view_post(client):
    response = client.post(
        reverse(url_names.project_create),
        {"name": "Programing", "description": "Programing project description"},
        follow=True,
    )
    assert response.status_code == 200
    project = Project.objects.first()
    assert project.name == "Programing"
    assert project.description == "Programing project description"


### Message View Tests
@pytest.mark.django_db
def test_message_create_view_post(client, project):
    response = client.post(
        reverse("message_create", args=(project.pk,)),
        {"title": "Learn CSS", "content": "learn css", "project": project.pk},
        follow=True,
    )
    assert response.status_code == 200
    message = Message.objects.filter(project=project).first()
    assert message.edited_at is not None


@pytest.mark.django_db
def test_correct_date_format(client, project):
    Message.objects.create(
        project=project,
        title="The title",
        edited_at=datetime(2020, 1, 15, 14, 15, 55, tzinfo=pytz.utc),
    )
