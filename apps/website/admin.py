from django.contrib import admin

from apps.website.models import Slider, WebsiteSettings


class SliderInline(admin.TabularInline):
    model = WebsiteSettings.slider.through
    extra = 3


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['title']
    exclude = ['slider']
    inlines = [SliderInline]