from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated

from src.server.repositories.messages import MessagesRepository
from src.server.schemas.messages import UserMessageSchemaAdd

# from src.server.api.dto.request import UserMessageDTO
from src.server.db.database import get_async_session

router = APIRouter(
    prefix='/messages',
    tags=['Messages'],
)

async_session = Annotated[
    AsyncSession,
    Depends(get_async_session),
]


@router.post('')
async def add_message(
    user_message: UserMessageSchemaAdd,
):
    user_message_dict = user_message.model_dump()
    user_message_id = await MessagesRepository().add_one(user_message_dict)
    return {'user_message_id': user_message_id}


@router.get('')
async def get_message(
    user_message: UserMessageSchemaAdd,
    session: async_session,
):
    pass
