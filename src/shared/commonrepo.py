from uuid import UUID
from tortoise.models import Model
import typing

Item = typing.TypeVar("Item", bound=Model)


class CommonRepo(typing.Generic[Item]):
    def __init__(self, item: typing.Type[Item]) -> None:
        super().__init__()
        self.item = item
        pass

    async def read_all(self) -> typing.List[Item]:
        return await self.item.all()

    async def read(self, id: UUID):
        return await self.item.get(id=id)

    async def insert(self, item: Item) -> Item:
        _item = self.item(**item.__dict__)
        await self.save(_item)
        return _item

    async def delete(self, id: UUID) -> None:
        _item = await self.read(id)
        await _item.delete()
        return None

    # FIXME: too long way to do this while passing model type
    # async def update(self, id: UUID, item: Item) -> None:
    #     keys = {k: v for k, v in item.__dict__.items(
    #     ) if not k.startswith("_") and k.lower() != "id"}
    #     print(keys)
    #     await self.item.filter(id=id).update(**keys)

    #     return None

    async def save(self, item: Item) -> None:
        await self.item.save(item)
        return
