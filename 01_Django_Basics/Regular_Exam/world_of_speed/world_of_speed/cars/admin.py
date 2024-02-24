from django.contrib import admin

from world_of_speed.cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_type', 'model', 'year', 'price', 'owner_name')

    def owner_name(self, obj):
        return obj.owner.full_name
