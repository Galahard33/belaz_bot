from typing import List

from . import models


async def get_info() -> [models.Info]:
    return await models.Info.all()


async def get_element(item_id) -> [models.Info]:
        return await models.Info.get(id=item_id)


async def get_contest() -> [models.Contest]:
    return await models.Contest.all().order_by('id')


async def get_element_contest (item_id) -> [models.Contest]:
    return await models.Contest.get(id=item_id)


async def get_add_info(item_id) -> [models.AdditionalInformation]:
    return await models.AdditionalInformation.get(id=item_id)
