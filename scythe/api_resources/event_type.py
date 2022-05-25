from scythe.api_resources.abstract import AbstractObject, AbstractResource, AbstractListObject
from typing import Dict, List


class EventType(AbstractResource):
    OBJECT_NAME = "event_type"
    attrs = ["code", "domain_id", "description"]

    def fetch(self, params: Dict) -> AbstractObject:
        return super().fetch(params)

    def list(self, **kwargs) -> AbstractListObject:
        return super().list(kwargs)

    def create(self, data: Dict) -> AbstractObject:
        return super().create(data)

    def update(self, data: Dict) -> AbstractObject:
        return super().update(data)

    def deactivate(self, data: Dict, api_key: str = None) -> AbstractObject:
        return super().deactivate(data, api_key)

    def activate(self, data: Dict, api_key: str = None) -> AbstractObject:
        return super().activate(data, api_key)
