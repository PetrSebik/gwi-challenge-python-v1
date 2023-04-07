from django.contrib import admin
from .models import Dinosaur, DinosaurMedia


# Register your models here.

@admin.register(Dinosaur)
class DinosaurAdmin(admin.ModelAdmin):
    pass


@admin.register(DinosaurMedia)
class DinosaurMediaAdmin(admin.ModelAdmin):
    pass
