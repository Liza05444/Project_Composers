from django.contrib import admin
from .models import GenreModel, ComposerModel, CompositionModel

# admin.site.register(ComposerModel)
class ComposerAdmin(admin.ModelAdmin):
	list_display = ('fio', 'biography', 'date_of_birth', 'date_of_death', 'photo')
	fields = ['fio', ('date_of_birth', 'date_of_death')]
	list_filter = ('fio', 'date_of_birth')

admin.site.register(ComposerModel, ComposerAdmin)
admin.site.register(CompositionModel)
admin.site.register(GenreModel)