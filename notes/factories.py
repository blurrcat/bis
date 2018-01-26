import factory
from .models import Note


class NoteFactory(factory.DjangoModelFactory):
    class Meta:
        model = Note

    content = factory.Faker('text')
