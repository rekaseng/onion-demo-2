from typing import List

from domain.models.coupon import Coupon
from domain.repositories.coupon_repository import CouponRepository
from application.dto.coupon_dto import CouponCreationDTO, CouponUpdateDTO


class CouponUseCases:
    def __init__(self, coupon_repository: CouponRepository):
        self.coupon_repository = coupon_repository

    async def add(self, coupon_dto: CouponCreationDTO) -> Coupon:
        coupon = Coupon(name=coupon_dto.name, code=coupon_dto.code, type=coupon_dto.type, discount = coupon_dto.discount,
                        logged = coupon_dto.logged, total = coupon_dto.total, date_start = coupon_dto.date_start,
                        date_end = coupon_dto.date_end, uses_total = coupon_dto.uses_total, uses_customer = coupon_dto.uses_customer,
                        status = coupon_dto.status, date_added = coupon_dto.date_added, skus = coupon_dto.skus, collections = coupon_dto.collections)
        await self.coupon_repository.add(coupon)
        return coupon

    async def get_all(self) -> List[Coupon]:
        coupons = await self.coupon_repository.get_all()
        return coupons

    async def get_by_code(self, code: str) -> Coupon:
        coupon = await self.coupon_repository.get_by_code(code)
        return coupon

    async def update_coupon(self, updatecoupon_dto: CouponUpdateDTO) -> None:
       await self.coupon_repository.update_coupon(updatecoupon_dto)

    async def delete_coupon(self, code: str) -> None:
        await self.coupon_repository.delete_coupon(code)