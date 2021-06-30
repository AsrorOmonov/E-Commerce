from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from my_admin.models import OutfitModel


def index(request):
    #

    q = request.POST.get('q')

    if q:
        data = OutfitModel.objects.filter(Q(title__icontains=q) | Q(brand__name__icontains=q)).order_by('pk')
    else:
        data = OutfitModel.objects.all()

    context = {
        'data': data
    }

    return render(request, 'index.html', context)


def detail(request, pk):
    data = get_object_or_404(OutfitModel, pk=pk)

    context = {
        'data': data
    }

    return render(request, 'detail.html', context)
