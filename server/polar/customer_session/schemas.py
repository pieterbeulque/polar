from datetime import datetime

from pydantic import UUID4, Field
from pydantic.aliases import AliasChoices

from polar.customer.schemas.customer import Customer
from polar.kit.schemas import IDSchema, Schema, TimestampedSchema


class CustomerSessionCustomerIDCreate(Schema):
    """
    Schema for creating a customer session using a customer ID.
    """

    customer_id: UUID4 = Field(
        description="ID of the customer to create a session for."
    )


class CustomerSessionCustomerExternalIDCreate(Schema):
    """
    Schema for creating a customer session using an external customer ID.
    """

    external_customer_id: str = Field(
        description="External ID of the customer to create a session for.",
        validation_alias=AliasChoices("external_customer_id", "customer_external_id"),
    )


CustomerSessionCreate = (
    CustomerSessionCustomerIDCreate | CustomerSessionCustomerExternalIDCreate
)


class CustomerSession(IDSchema, TimestampedSchema):
    """
    A customer session that can be used to authenticate as a customer.
    """

    token: str = Field(validation_alias="raw_token")
    expires_at: datetime
    customer_portal_url: str
    customer_id: UUID4
    customer: Customer
