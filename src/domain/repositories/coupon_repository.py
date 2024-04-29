from abc import ABC, abstractmethod
from typing import Optional, List
from domain.models.coupon import Coupon, UpdateCoupon


class CouponRepository(ABC):
    @abstractmethod
    async def add(self, coupon: Coupon) -> None:
        pass

    @abstractmethod
    async def get_by_code(self, code: str) -> Optional[Coupon]:
        pass

    @abstractmethod
    async def get_all(self) -> List[Coupon]:
        pass

    @abstractmethod
    async def update_coupon(self, updateCoupon: UpdateCoupon) -> None:
        pass

    @abstractmethod
    async def delete_coupon(self, code: str) -> None:
        pass