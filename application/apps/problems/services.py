from typing import Tuple

from . import models


async def get_info() -> [models.ProblemsModel]:
    return await models.ProblemsModel.all()


async def add_problems(name, descriptions, photo):
    return await models.ProblemsModel.create(
        name=name, descriptions=descriptions, photo=photo
    )


async def get_item(item_id) -> [models.ProblemsModel]:
    return await models.ProblemsModel.get(id=item_id)
