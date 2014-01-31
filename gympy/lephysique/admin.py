from django.contrib import admin
from lephysique.models import Card, Exercise, Series, Repetitions, Executions, Rest, Exercise1, Exercise2, Exercise3, Exercise4, Exercise5



class Exercise1Inline(admin.TabularInline):
    model = Exercise1

class Exercise2Inline(admin.TabularInline):
    model = Exercise2

class Exercise3Inline(admin.TabularInline):
    model = Exercise3

class Exercise4Inline(admin.TabularInline):
    model = Exercise4

class Exercise5Inline(admin.TabularInline):
    model = Exercise5


class CardAdmin(admin.ModelAdmin):
    inlines = [Exercise1Inline, Exercise2Inline, Exercise3Inline, Exercise4Inline, Exercise5Inline]
    search_fields=['surname', 'name']
    save_as = True



admin.site.register(Card,CardAdmin)

admin.site.register(Exercise)
admin.site.register(Series)
admin.site.register(Repetitions)
admin.site.register(Executions)
admin.site.register(Rest)