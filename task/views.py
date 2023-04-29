from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from task.forms import TagForm, TaskForm
from task.models import Task, Tag


class HomePageView(generic.ListView):
    model = Task
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("pk")
        task = Task.objects.get(id=pk)
        task.status_done = not task.status_done
        task.save()
        return HttpResponseRedirect(self.request.path_info)


class CreateNewTask(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("home")
    template_name = "task_form.html"


class UpdateTaskView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("home")
    template_name = "task_form.html"


class DeleteTaskView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("home")
    template_name = "delete_task.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "tags.html"


class CreateNewTag(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("home")
    template_name = "task_form.html"


class UpdateTagView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("home")
    template_name = "task_form.html"


class DeleteTagView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("home")
    template_name = "delete_task.html"
