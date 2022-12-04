from typing import Any, Dict, Optional

from ..objects.customer import Customer
from .base import ResourceCreateMixin, ResourceDeleteMixin, ResourceGetMixin, ResourceListMixin, ResourceUpdateMixin


class Customers(ResourceCreateMixin, ResourceDeleteMixin, ResourceGetMixin, ResourceListMixin, ResourceUpdateMixin):
    """Resource handler for the `/customers` endpoint."""

    RESOURCE_ID_PREFIX: str = "cst_"
    RESULT_CLASS_PATH: str = "mollie.api.objects.customer.Customer"

    def get(self, resource_id: str, **params: Any) -> Customer:
        self.validate_resource_id(resource_id, "customer ID")
        return super().get(resource_id, **params)

    def update(self, resource_id: str, data: Optional[Dict[str, Any]] = None, **params: Any) -> Customer:
        self.validate_resource_id(resource_id, "customer ID")
        return super().update(resource_id, data, **params)

    def delete(self, resource_id: str, **params: Any) -> dict:
        self.validate_resource_id(resource_id, "customer ID")
        return super().delete(resource_id, **params)
