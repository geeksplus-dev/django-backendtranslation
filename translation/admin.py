from django.contrib import admin
from django.contrib import admin
from .models import TranslationKey, Translation
from .forms import AtLeastOneRequiredInlineFormSet
# Register your models here.


class TranslationInline(admin.TabularInline):
    model = Translation
    formset = AtLeastOneRequiredInlineFormSet


class TranslationKeyAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = TranslationKey.objects.prefetch_related('translation_set').all()
        return qs
    inlines = [
        TranslationInline
    ]


admin.site.register(TranslationKey, TranslationKeyAdmin)
