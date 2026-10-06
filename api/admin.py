from django.contrib import admin
from .models import (
    Conference,
    Shoba,
    Maqola,
    AboutShoba,
    WordPart
)


class WordPartInline(admin.TabularInline):
    model = WordPart
    extra = 1
    fields = ('maqola_soni', 'bet_soni', 'word_fayl', 'yaratilgan_sana')
    readonly_fields = ('yaratilgan_sana',)


class ShobaInline(admin.TabularInline):
    model = Shoba
    extra = 1
    fields = ('title', 'is_active', 'yaratilgan_sana')
    readonly_fields = ('yaratilgan_sana',)
    show_change_link = True  


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'slug')
    search_fields = ('title', 'type')
    inlines = [WordPartInline, ShobaInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('slug',)
        return self.readonly_fields

    def get_prepopulated_fields(self, request, obj=None):
        if not obj:
            return {'slug': ('title',)}
        return {}



class MaqolaInline(admin.TabularInline):
    model = Maqola
    extra = 1
    fields = ('title', 'word_fayl', 'yaratilgan_sana')
    readonly_fields = ('yaratilgan_sana',)


class AboutShobaInline(admin.StackedInline):  
    model = AboutShoba
    extra = 0
    max_num = 1  
    readonly_fields = ('yaratilgan_sana',)


@admin.register(Shoba)
class ShobaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'conference', 'is_active', 'yaratilgan_sana')
    list_filter = ('is_active', 'conference', 'yaratilgan_sana')
    search_fields = ('title', 'conference__title')
    inlines = [MaqolaInline, AboutShobaInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('slug',)
        return self.readonly_fields

    def get_prepopulated_fields(self, request, obj=None):
        if not obj:
            return {'slug': ('title',)}
        return {}



@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'shoba', 'yaratilgan_sana')
    list_filter = ('shoba__conference', 'shoba', 'yaratilgan_sana')
    search_fields = ('title', 'shoba__title')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('slug',)
        return self.readonly_fields

    def get_prepopulated_fields(self, request, obj=None):
        if not obj:
            return {'slug': ('title',)}
        return {}


@admin.register(AboutShoba)
class AboutShobaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'shoba', 'maqola_soni', 'yaratilgan_sana')
    search_fields = ('title', 'shoba__title')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('slug',)
        return self.readonly_fields

    def get_prepopulated_fields(self, request, obj=None):
        if not obj:
            return {'slug': ('title',)}
        return {}


@admin.register(WordPart)
class WordPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'conference', 'maqola_soni', 'bet_soni', 'yaratilgan_sana')
    list_filter = ('yaratilgan_sana', 'conference')
    search_fields = ('conference__title',)