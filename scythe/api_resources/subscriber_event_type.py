from scythe.api_resources.abstract import AbstractObject, AbstractResource, AbstractListObject
from typing import Dict, List


class SubscriberEventType(AbstractResource):
    OBJECT_NAME = "subscriber_event_type"
    attrs = ["subscriber_url_id", "event_type_id", "access_key", "description"]

    def fetch(self, params: Dict) -> AbstractObject:
        return super().fetch(params)

    def list(self, **kwargs) -> AbstractListObject:
        return super().list(kwargs)

    def create(self, data: Dict) -> AbstractObject:
        return super().create(data)

    def update(self, data: Dict) -> AbstractObject:
        return super().update(data)

    def delete(self, data: Dict) -> AbstractObject:
        return super().delete(data)
