from sqlalchemy import and_

from database.settings import ConnectionDatabase
from database.models.bank import Notification as NotificationModel


class NotificationAlchemyAdapter(ConnectionDatabase):
    def __init__(self):
        super().__init__()

    def create(self, title: str, describe: str):
        notification = NotificationModel(
            title=title,
            describe=describe,)
        self.session.add(notification)
        self.session.commit()
        self.session.refresh(notification)
        self.session.close()
        return notification

    def get_by_id(self, entity_id: int):
        notification = self.session.query(NotificationModel).filter(
            and_(NotificationModel.is_active is True,
                 NotificationModel.entity_id == entity_id))
        self.session.close()
        return notification

    def get_all(self):
        notifications = self.session.query(NotificationModel).filter(
            NotificationModel.is_active == True).all()
        self.session.close()
        return notifications

    def delete_by_id(self, entity_id):
        notification = self.session.query(NotificationModel).filter_by(
            entity_id=entity_id).first()

        notification.is_active = False

        self.session.commit()
        self.session.refresh(notification)
        self.session.close()
        return notification

    def read(self, entity_id: int):
        notification = self.session.query(NotificationModel).filter_by(
            entity_id=entity_id).first()

        notification.is_read = True

        self.session.commit()
        self.session.refresh(notification)
        self.session.close()
        return notification
