import pytest
from bis.factories import UserFactory
from notes.models import Note
from notes.factories import NoteFactory


@pytest.mark.django_db
def test_create(harry, harry_client):
    resp = harry_client.post('/v1/notes/', data={
        'content': 'todo1',
    })
    assert resp.status_code == 201
    note = Note.objects.get(id=resp.data['id'])
    assert note.created_at and note.updated_at
    assert note.author == harry


@pytest.mark.django_db
def test_list(harry, harry_client):
    resp = harry_client.get('/v1/notes/')
    assert resp.status_code == 200
    assert resp.data == []
    n1 = NoteFactory.create(author=harry)
    other_people = UserFactory.create()
    NoteFactory.create(author=other_people)
    # should only list my notes
    resp = harry_client.get('/v1/notes/')
    assert resp.status_code == 200
    assert len(resp.data) == 1
    assert resp.data[0]['id'] == n1.id
