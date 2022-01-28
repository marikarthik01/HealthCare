from django.contrib import admin
from .models import Category
from .models import Products
# Register your models here.


admin.site.register([Category,Products])