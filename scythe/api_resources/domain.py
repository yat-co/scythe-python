from scythe.api_resources.abstract import AbstractObject, AbstractResource
from typing import Dict, List


class Domain(AbstractResource):
    OBJECT_NAME = "domain"
    attrs = ["code", "description"]

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
