from database.adapters.notification import NotificationAlchemyAdapter
from lib.schemas.notification_schemas import NotificationSchema


class PostNotificationResponseModel:
    def __init__(self, notification):
        self.notification = notification

    def __call__(self):
        return self.notification.to_json()


class PostNotificationRequestModel:
    def __init__(self, notification: NotificationSchema):
        self.title = notification.title
        self.describe = notification.describe


class PostNotificationInteractor:
    def __init__(self,
                 request: PostNotificationRequestModel,
                 adapter: NotificationAlchemyAdapter):
        self.request = request
        self.adapter = adapter

    def create_notification(self):
        notification = self.adapter.create(
            title=self.request.title,
            describe=self.request.describe,)
        return notification

    def run(self):
        notification = self.create_notification()
        response = PostNotificationResponseModel(notification)
        return response
