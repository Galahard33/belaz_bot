from django.contrib import admin

from .. import models


@admin.register(models.Info.DjangoModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contest.DjangoModel)
class ContestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AdditionalInformation.DjangoModel)
class AddinfoAdmin(admin.ModelAdmin):
    pass