from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str = Field(...)
    price: float = Field(...)
    quantity: int = Field(...)

class ProductResponse(Product):
    id: str

class UpdateProduct(BaseModel):
    name: Optional[str]
    price: Optional[float]
    quantity: Optional[int]