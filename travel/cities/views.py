from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from cities.forms import CityForm
from cities.models import City

__all__ = (
    "home",
    "CityDetailView",
    "CityCreateView",
    "CityUpdateView",
    "CityDeleteView",
    "CityListView",
)


def home(request, pk=None):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 2)
    page_numder = request.GET.get('page')
    page_obj = lst.get_page(page_numder)
    context = {'page_obj': page_obj, 'objects_list': qs, 'form': form}
    return render(request, "cities/home.html", context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail.html"


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = "cities/create.html"
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно создан"


class CityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = "cities/update.html"
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно отредактирован"


class CityDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = City
    template_name = "cities/delete.html"
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно удален"


class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = "cities/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context
