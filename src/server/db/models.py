from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func
import datetime

from src.server.db.database import Base
from src.server.schemas.messages import UserMessageSchema


class ChatMessage(Base):
    __tablename__ = 'chat_messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    message: Mapped[str]
    sent_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    def to_read_model(self) -> UserMessageSchema:
        return UserMessageSchema(
            id=self.id,
            username=self.username,
            message=self.message,
            sent_at=self.sent_at,
        )
