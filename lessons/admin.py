from django.contrib import admin

from lessons.models import Lesson, Translation


class TranslationInline(admin.StackedInline):
    model = Translation


class LessonAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_list.html"
    date_hierarchy = "created_at"
    inlines = [TranslationInline]
    list_display = ("published", "order", "title", "updated_at")
    list_display_links = ("title",)
    list_editable = ("order", "published")
    list_filter = ("published", "created_at", "updated_at")
    search_fields = ("title",)

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Translation)
