from django.contrib import admin

from .. import models


@admin.register(models.ProblemsModel.DjangoModel)
class ProblemAdmin(admin.ModelAdmin):
    pass