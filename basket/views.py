from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ A view to return the basket contents page """
    template = 'basket/basket.html'
    return render(request, template)
