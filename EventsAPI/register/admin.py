from django.contrib import admin
from .models import Register

# Register your models here.
#admin.site.register(Register)


#admin.site.register(Register)

@admin.register(Register)
class registerAdmin(admin.ModelAdmin):
      fields = ('username', 'full_name', 'address', 'city')
      list_display = ('username', 'full_name', 'address', 'city')
      ordering = ('full_name',)