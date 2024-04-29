from typing import Optional, List
from pydantic import BaseModel
from datetime import date

class Coupon(BaseModel):
    id: Optional[int] = None
    name: str
    code: str
    type: str
    discount: float
    logged: bool
    total: float
    date_start: date
    date_end: date
    uses_total: int
    uses_customer: str
    status: bool = True
    date_added: date
    skus: Optional[List[int]] = None
    collections: Optional[List[int]] = None

class UpdateCoupon(BaseModel):
    id: Optional[int] = None
    name: str
    code: str
    type: str
    discount: float
    logged: bool
    total: float
    date_start: date
    date_end: date
    uses_total: int
    uses_customer: str
    status: bool = True
    skus: Optional[List[int]] = None
    collections: Optional[List[int]] = None


