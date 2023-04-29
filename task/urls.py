from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from task.views import HomePageView, CreateNewTask, UpdateTaskView,\
  DeleteTaskView, TagListView, DeleteTagView, UpdateTagView,\
  CreateNewTag


urlpatterns = [
  path("", HomePageView.as_view(), name="home"),
  path("create-new-task/", CreateNewTask.as_view(), name="new-task"),
  path("<int:pk>/update/", UpdateTaskView.as_view(), name="update-task"),
  path("<int:pk>/delete/", DeleteTaskView.as_view(), name="delete-task"),
  path("tag/", TagListView.as_view(), name="tags"),
  path("tag/create-new-tag/", CreateNewTag.as_view(), name="new-tag"),
  path("tag/<int:pk>/update/", UpdateTagView.as_view(), name="update-tag"),
  path("tag/<int:pk>/delete/", DeleteTagView.as_view(), name="delete-tag"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
