from django.contrib import admin

# Register your models here.

from .models import Category, Projects

class ProjAdmin(admin.ModelAdmin):
    list_display = ('title','description','url','category')
    list_display_links = ('title','description')
    search_fields = ('title','description')
    
admin.site.register(Projects, ProjAdmin)
admin.site.register(Category)

# login - hellcard
# password - 123 
# :))