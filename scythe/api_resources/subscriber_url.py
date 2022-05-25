from scythe.api_resources.abstract import AbstractObject, AbstractResource
from typing import Dict, List


class SubscriberUrl(AbstractResource):
    OBJECT_NAME = "subscriber_url"
    attrs = ["subscriber_id", "url", "access_key", "description"]

    def fetch(self, params: Dict) -> AbstractObject:
        return super().fetch(params)

    def list(self, params: Dict = None) -> List[AbstractObject]:
        return super().list(params)

    def create(self, data: Dict) -> AbstractObject:
        return super().create(data)

    def update(self, data: Dict) -> AbstractObject:
        return super().update(data)

    def delete(self, data: Dict) -> AbstractObject:
        return super().delete(data)
