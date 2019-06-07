from django.contrib import admin

from applications.core import models

admin.site.register(models.Category)
admin.site.register(models.Subcategory)
admin.site.register(models.Enterprise)
admin.site.register(models.Product)
admin.site.register(models.Discounts)
admin.site.register(models.Contact)
admin.site.register(models.PageCounter)
