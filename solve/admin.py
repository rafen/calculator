from django.contrib import admin
from solve.models import Equation, Session


class SessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_search = ['name']


class EquationAdmin(admin.ModelAdmin):
    list_display = ['command', 'result']


admin.site.register(Session, SessionAdmin)
admin.site.register(Equation, EquationAdmin)
