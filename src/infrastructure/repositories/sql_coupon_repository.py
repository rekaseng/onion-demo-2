from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from domain.models.coupon import Coupon, UpdateCoupon
from domain.repositories.coupon_repository import CouponRepository
from infrastructure.orm.coupon_orm_model import CouponOrmModel
from fastapi import HTTPException


class SQLCouponRepository(CouponRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_all(self) -> List[Coupon]:
        result = await self.db_session.execute(select(CouponOrmModel))
        orm_coupons = result.scalars().all()
        coupons = [item.to_domain() for item in orm_coupons]
        return coupons

    async def add(self, coupon: Coupon) -> None:
        coupon_result = await self.db_session.execute(select(CouponOrmModel).filter_by(code=coupon.code))
        orm_coupon = coupon_result.scalars().first()

        if orm_coupon:
            raise HTTPException(status_code=409, detail="Coupon with this code already exists")

        orm_coupon = CouponOrmModel.from_domain(coupon)
        await self.db_session.merge(orm_coupon)
        await self.db_session.commit()

    async def get_by_code(self, code: str) -> Coupon:
        result = await self.db_session.execute(select(CouponOrmModel).filter(CouponOrmModel.code == code))
        orm_coupon = result.scalars().first()

        if orm_coupon is None:
            raise HTTPException(status_code=404, detail="Coupon not found")

        coupon = orm_coupon.to_domain()
        return coupon

    async def update_coupon(self, update_coupon: UpdateCoupon) -> None:
        coupon_result = await self.db_session.execute(select(CouponOrmModel).filter_by(code=update_coupon.code))
        orm_coupon = coupon_result.scalars().first()

        if orm_coupon is None:
            raise HTTPException(status_code=404, detail="Coupon not found")

        orm_coupon.name = update_coupon.name
        orm_coupon.type = update_coupon.type
        orm_coupon.discount = update_coupon.discount
        orm_coupon.logged = update_coupon.logged
        orm_coupon.total = update_coupon.total
        orm_coupon.date_start = update_coupon.date_start
        orm_coupon.date_end = update_coupon.date_end
        orm_coupon.status = update_coupon.status
        orm_coupon.skus = update_coupon.skus
        orm_coupon.collections = update_coupon.collections

        await self.db_session.commit()

    async def delete_coupon(self, code: str) -> None:
        coupon_result = await self.db_session.execute(select(CouponOrmModel).filter_by(code=code))
        orm_coupon = coupon_result.scalars().first()

        if orm_coupon is None:
            raise HTTPException(status_code=404, detail="Coupon not found")

        await self.db_session.delete(orm_coupon)
        await self.db_session.commit()