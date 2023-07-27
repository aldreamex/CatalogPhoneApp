from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    all_phones = Phone.objects.all()
    if sort_pages == 'low':
        all_phones = all_phones.order_by('price')
    elif sort_pages == 'high':
        all_phones = all_phones.order_by('-price')
    elif sort_pages == 'alph':
        all_phones = all_phones.order_by('name')
    context = {'phones': all_phones}
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
    except Phone.DoesNotExist:
        raise Http404("Телефон не найден")

    context = {'phone': phone}
    return render(request, template, context=context)
