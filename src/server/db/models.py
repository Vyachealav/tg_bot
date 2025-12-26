from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime
import datetime

from server.db.database import Base



class ChatMessage(Base):
    __tablename__ = 'chat_messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    message: Mapped[str]
    sent_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    sent_at: Mapped[datetime.datetime] = mapped_column(DateTime)
