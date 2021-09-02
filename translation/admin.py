from django.contrib import admin
from django.contrib import admin
from .models import TranslationKey, Translation
from .forms import AtLeastOneRequiredInlineFormSet
# Register your models here.


class TranslationInline(admin.TabularInline):
    model = Translation
    formset = AtLeastOneRequiredInlineFormSet


class TranslationKeyAdmin(admin.ModelAdmin):
    def queryset(self, request, queryset):
        qs = TranslationKey.objects.prefetch_related('translation_set').all()
    inlines = [
        TranslationInline
    ]


admin.site.register(TranslationKey, TranslationKeyAdmin)
