from orm_converter.tortoise_to_django import ConvertedModel
from tortoise import Tortoise, fields
from tortoise.models import Model


class ProblemsModel(Model, ConvertedModel):
    name = fields.CharField(max_length=255)
    photo = fields.CharField(max_length=255)
    descriptions = fields.TextField()

    class Meta:
        table = "problems"

    def __str__(self) -> str:
        return self.name


def register_models() -> None:
    Tortoise.init_models(
        models_paths=["apps.problems.models"],
        app_label="problems",
        _init_relations=False,
    )
