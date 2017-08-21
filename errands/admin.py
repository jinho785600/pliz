from django.contrib import admin
from errands.models import Errand
from errands.models import Candidate

# Register your models here.

class CandidateInline(admin.StackedInline):
    model = Candidate

class ErrandAdmin(admin.ModelAdmin):
    fields = ('owner','category', 'title', 'text','extraCost','reward',)
    inlines = [CandidateInline,]


admin.site.register(Errand, ErrandAdmin)