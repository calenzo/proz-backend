from fastapi import APIRouter

from lib.interactors.post_notification_interactor import (
    PostNotificationRequestModel,
    PostNotificationInteractor,
)

from lib.interactors.delete_notification_interactor import (
    DeleteNotificationRequestModel,
    DeleteNotificationInteractor,
)

from lib.interactors.get_notifications_interactor import (
    GetNotificationsInteractor,
)

from lib.interactors.read_notification_interactor import (
    ReadNotificationRequestModel,
    ReadNotificationInteractor,
)

from lib.schemas.notification_schemas import NotificationSchema

from database.adapters.notification import NotificationAlchemyAdapter

router = APIRouter()


@router.post('/notification')
def post_notification(notification: NotificationSchema):
    request = PostNotificationRequestModel(notification)
    interactor = PostNotificationInteractor(request,
                                            NotificationAlchemyAdapter())

    result = interactor.run()

    return result()


@router.get('/notifications')
def post_notification():
    interactor = GetNotificationsInteractor(NotificationAlchemyAdapter())

    result = interactor.run()

    return result()


@router.delete('/notification/{entity_id}')
def delete_notification(entity_id):
    request = DeleteNotificationRequestModel(entity_id)
    interactor = DeleteNotificationInteractor(request,
                                              NotificationAlchemyAdapter())

    result = interactor.run()

    return result()


@router.patch('/notification/{entity_id}/read')
def read_notification(entity_id):
    request = ReadNotificationRequestModel(entity_id)
    interactor = ReadNotificationInteractor(request,
                                            NotificationAlchemyAdapter())

    result = interactor.run()

    return result()
