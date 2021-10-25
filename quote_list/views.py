from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Quote

def listing(request):
    quote_list = Quote.objects.all()
    paginator = Paginator(quote_list, 25) # Show 25 Quotes per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main.html', {'page_obj': page_obj})
