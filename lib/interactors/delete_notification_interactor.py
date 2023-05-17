from database.adapters.notification import NotificationAlchemyAdapter
from lib.schemas.notification_schemas import NotificationSchema


class DeleteNotificationResponseModel:
    def __init__(self):
        pass

    def __call__(self):
        return {
            "success": True
        }


class DeleteNotificationRequestModel:
    def __init__(self, entity_id: int):
        self.entity_id = entity_id


class DeleteNotificationInteractor:
    def __init__(self,
                 request: DeleteNotificationRequestModel,
                 adapter: NotificationAlchemyAdapter):
        self.request = request
        self.adapter = adapter

    def delete_notification(self):
        self.adapter.delete_by_id(self.request.entity_id)

    def run(self):
        self.delete_notification()
        response = DeleteNotificationResponseModel()
        return response
