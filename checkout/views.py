from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('basket', {})
    if not bag:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JublvI9PtSlElQm9mlSNhKq6JQ1An2WgwYe0PaWOdpGWHFpkg0xi4kEygAl3GE5B1NjDnvozXwzIe8yMkAePVlI00ON21TiYO',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
