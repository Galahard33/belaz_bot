from orm_converter.tortoise_to_django import ConvertedModel
from tortoise import Tortoise, fields
from tortoise.models import Model


class Info(Model, ConvertedModel):
    title = fields.CharField(max_length=255, description='Название цеха')
    text = fields.TextField( description='Подробная информация')
    latitude = fields.CharField(max_length=100, description='широта', null=True)
    longitude = fields.CharField(max_length=100, description='долгота', null=True)


    class Meta:
        table = "info"

    def __str__(self) -> str:
        return self.title


class Contest(Model, ConvertedModel):
    title = fields.CharField(max_length=255, description='Название конкурса')
    document_name = fields.CharField(max_length=255, description='Название документа', null=True)
    text = fields.TextField( description='Краткое описание', null=True)

    class Meta:
        table = "contest"

    def __str__(self) -> str:
        return self.title


class AdditionalInformation(Model, ConvertedModel):
    title = fields.CharField(max_length=255, description='Название раздела')
    text = fields.TextField( description='Информация о разделе')


    class Meta:
        table = "addinfo"

    def __str__(self) -> str:
        return self.title


def register_models() -> None:
    Tortoise.init_models(
        models_paths=["apps.hidden_app.models"],
        app_label="hidden_app",
        _init_relations=False,
    )
