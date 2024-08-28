from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        is_main_flag = False
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                if is_main_flag == True:
                    raise ValidationError(
                        'Двух главных тегов в статье быть не может')
                else:
                    is_main_flag = True
        if is_main_flag == False:
            raise ValidationError(
                    'Должен быть один и только один главный тег')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
