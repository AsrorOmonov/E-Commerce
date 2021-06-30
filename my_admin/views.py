from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from my_admin.forms import OutfitModelForm
from my_admin.models import OutfitModel


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


def detail(request, pk):
    data = get_object_or_404(OutfitModel, pk=pk)

    context = {
        'data': data
    }

    return render(request, 'my_admin/detail.html', context)


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


def delete(request, pk):
    data = get_object_or_404(OutfitModel, pk=pk)
    data.delete()
    return redirect('/my_admin/')
