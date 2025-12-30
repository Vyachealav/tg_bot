from src.server.db.models import ChatMessage
from server.utils.base import SQLAlchemyRepository


class MessagesRepository(SQLAlchemyRepository):
    model = ChatMessage
