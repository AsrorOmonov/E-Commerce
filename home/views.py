from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView

from my_admin.models import OutfitModel, BrandModel


def index(request):
    #

    q = request.POST.get('q')

    if q:
        data = OutfitModel.objects.filter(Q(title__icontains=q) | Q(brand__name__icontains=q)).order_by('pk')
    else:
        data = OutfitModel.objects.all()

    brand = BrandModel.objects.all()

    context = {
        'data': data,
        'brand': brand
    }

    return render(request, 'index.html', context)


# class OutfitTemplateView(TemplateView):
#     template_name = 'index.html'
#     model = OutfitModel
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = BrandModel.objects.all()

class OutfitListView(ListView):
    template_name = 'index.html'

    def get_queryset(self):

        q = self.request.POST.get('q')

        data = OutfitModel.objects.all()

        if q:
            data = data.filter(Q(title__icontains=q))
        else:
            data = OutfitModel.objects.all()
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = OutfitModel.objects.all()


def detail(request, pk):
    data = get_object_or_404(OutfitModel, pk=pk)
    brand = BrandModel.objects.all()
    context = {
        'data': data,
        'brand': brand
    }

    return render(request, 'detail.html', context)


class OutfitDetailView(DetailView):
    template_name = 'detail.html'
    model = OutfitModel
