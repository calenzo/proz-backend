from database.adapters.notification import NotificationAlchemyAdapter


class GetNotificationsResponseModel:
    def __init__(self, notifications):
        self.notifications = notifications

    def __call__(self):
        return self.notifications


class GetNotificationsInteractor:
    def __init__(self, adapter: NotificationAlchemyAdapter):
        self.adapter = adapter

    def get_notifications(self):
        notifications = self.adapter.get_all()
        return notifications

    def run(self):
        notifications = self.get_notifications()
        response = GetNotificationsResponseModel(notifications)
        return response
