from django.contrib import admin

from product.models import *

# products/admin.py
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ContactRequest)
admin.site.register(Client)



