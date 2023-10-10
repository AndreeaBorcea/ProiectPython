from product.models import Category
from product.views import get_open_cart


def nav_common_data(request):
    total_items = 0
    if request.user.is_authenticated:
        open_cart = get_open_cart(request)
        quantities = [c.quantity for c in open_cart.cart_items() ]
        total_items = sum(quantities)
    return {'categories': Category.objects.all(), 'total_items':total_items}
