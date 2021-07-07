from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from my_admin.forms import OutfitModelForm
from my_admin.models import OutfitModel


@login_required
def index(request):
    q = request.GET.get('q')
    if q:
        outfit = OutfitModel.objects.filter(Q(title__icontains=q) | Q(brand__name__icontains=q)).order_by('pk')
    else:
        outfit = OutfitModel.objects.all()

    context = {
        'outfit': outfit
    }

    return render(request, 'my_admin/index.html', context)


class AdminListView(ListView):
    template_name = 'my_admin/index.html'

    def get_queryset(self):
        get_data = self.request.GET
        q = get_data.get('q')
        if q:
            outfit = OutfitModel.objects.filter(Q(title__icontains=q))
        else:
            outfit = OutfitModel.objects.all()
        return outfit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfit'] = OutfitModel.objects.all()
        return context


@login_required
def detail(request, pk):
    data = get_object_or_404(OutfitModel, pk=pk)
    context = {
        'data': data
    }

    return render(request, 'my_admin/detail.html', context)


class OutfitDetailView(DetailView):
    template_name = 'my_admin/detail.html'
    model = OutfitModel
    context_object_name = 'data'


@login_required
def create(request):
    if request.method == 'POST':
        form = OutfitModelForm(request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

        return redirect('/my_admin/')

    else:

        form = OutfitModelForm()

        context = {
            'form': form

        }

        return render(request, 'my_admin/form.html', context)


class OutfitCreateView(CreateView):
    template_name = 'my_admin/form.html'
    form_class = OutfitModelForm
    success_url = '/my_admin/'


@login_required
def edit(request, pk):
    data = get_object_or_404(OutfitModel, pk=pk)

    if request.method == 'POST':
        form = OutfitModelForm(request.POST, files=request.FILES, instance=data)

        if form.is_valid():
            form.save()

            return redirect('/my_admin/')

    else:

        form = OutfitModelForm(instance=data)

        context = {
            'form': form
        }
        return render(request, 'my_admin/form.html', context)


class OutfitUpdateView(UpdateView):
    template_name = 'my_admin/form.html'
    form_class = OutfitModelForm
    success_url = '/my_admin/'
    model = OutfitModel  # we need it to fill the form with data out of the model


@login_required
def delete(request, pk):
    data = get_object_or_404(OutfitModel, pk=pk)
    data.delete()
    return redirect('/my_admin/')


class OutfitDeleteView(DeleteView):
    model = OutfitModel
    success_url = '/my_admin/'
