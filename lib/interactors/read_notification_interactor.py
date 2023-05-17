from database.adapters.notification import NotificationAlchemyAdapter
from lib.schemas.notification_schemas import NotificationSchema


class ReadNotificationResponseModel:
    def __init__(self, notification):
        self.notification = notification

    def __call__(self):
        return self.notification.to_json()


class ReadNotificationRequestModel:
    def __init__(self, entity_id):
        self.entity_id = entity_id


class ReadNotificationInteractor:
    def __init__(self,
                 request: ReadNotificationRequestModel,
                 adapter: NotificationAlchemyAdapter):
        self.request = request
        self.adapter = adapter

    def read_notification(self):
        notification = self.adapter.read(self.request.entity_id)
        return notification

    def run(self):
        notification = self.read_notification()
        response = ReadNotificationResponseModel(notification)
        return response
