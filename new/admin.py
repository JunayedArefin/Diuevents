from django.contrib import admin
from .models import Contact
from .models import Category, Post


#for config of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Register your models here.

admin.site.register(Contact)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)