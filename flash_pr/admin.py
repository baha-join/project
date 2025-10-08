from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Sellers)
admin.site.register(Games)
admin.site.register(Reviews)
admin.site.register(Orders)
admin.site.register(OrderItems)