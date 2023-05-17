from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime

from database.settings import Base


class Notification(Base):
    __tablename__ = "TB_NOTIFICATION"

    entity_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    describe = Column(String(255))
    is_read = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def to_json(self):
        return vars(self)
