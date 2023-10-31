from django.contrib import admin
from AkaliAlimentosApp import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.OrderToProduct)
admin.site.register(models.Contact)