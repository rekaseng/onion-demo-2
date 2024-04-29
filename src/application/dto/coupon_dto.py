from pydantic import BaseModel
from typing import List
from datetime import date

class CouponCreationDTO(BaseModel):
    name: str
    code: str
    type: str
    discount: float
    logged: bool
    total: float
    date_start: date
    date_end: date
    uses_total: float
    uses_customer: str
    status: bool
    date_added: date
    skus: List[int]
    collections: List[int]

class CouponUpdateDTO(BaseModel):
    name: str
    code: str
    type: str
    discount: float
    logged: bool
    total: float
    date_start: date
    date_end: date
    status: bool
    skus: List[int]
    collections: List[int]
