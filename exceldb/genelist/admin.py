from django.contrib import admin

from .models import Literature, Gene

@admin.register(Literature)
class LiteratureAdmin(admin.ModelAdmin):
    pass

@admin.register(Gene)
class GeneAdmin(admin.ModelAdmin):
    pass
