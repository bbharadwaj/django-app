from django.contrib import admin
from coltrane.models import Category
from coltrane.models import Entry

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
	
admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Entry, EntryAdmin)
