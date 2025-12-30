from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from src.server.db.database import async_session_factory


class AbstractRepository(ABC):
    @abstractmethod
    async def add_many():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_many(self, data: list[dict]) -> list[int]:
        async with async_session_factory() as session:
            stmt = insert(self.model).values(data).returning(self.model.id)

            res = await session.execute(stmt)
            await session.commit()

            return res.scalars().all()

    async def find_all(self):
        async with async_session_factory() as session:
            stmt = select(self.model)

            res = await session.execute(stmt)

            return [row[0].to_read_model() for row in res.all()]
