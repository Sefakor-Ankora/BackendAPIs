from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(User)

#@admin.register(User)
#class UserAdmin(admin.ModelAdmin):
      #fields = ('email', 'username', )
      #list_display = (  'email', 'username')
      #ordering = ('email',)
      #search_fields = ('username',)

