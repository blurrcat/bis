from rest_framework.routers import SimpleRouter
from notes.views import NoteViewSet


api_router = SimpleRouter()
api_router.register('notes', NoteViewSet, base_name='notes')

urlpatterns = api_router.urls
