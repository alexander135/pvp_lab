from django.contrib import admin
from .models import Recipe
from .models import Like
from .models import Comment
from .models import Ingredient

from .models import Complaint

class ComplaintInLine(admin.TabularInline):
    model = Complaint


class RecipeAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', )
    inlines = [
       ComplaintInLine,
]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Complaint)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Ingredient)

