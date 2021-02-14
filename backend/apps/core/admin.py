from django.contrib import admin

from apps.core.models import Solution


class SolutionAdmin(admin.ModelAdmin):
    list_filter = ('start_dt', 'status')
    list_display = ('start_dt', 'status')

    def get_readonly_fields(self, request, obj=None):
        return list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]  # in case we somehow extend our model
        ))

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Solution, SolutionAdmin)
