from src.server.db.models import ChatMessage
from src.server.utils.repository import SQLAlchemyRepository


class MessagesRepository(SQLAlchemyRepository):
    model = ChatMessage
