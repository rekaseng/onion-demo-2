from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from application.dto.coupon_dto import CouponCreationDTO, CouponUpdateDTO
from api.deps import get_db
from application.use_cases.coupon_use_cases import CouponUseCases
from domain.models.coupon import Coupon
from infrastructure.repositories.sql_coupon_repository import SQLCouponRepository

router = APIRouter()

@router.post("/", response_model=Coupon)
async def coupon_add(
        coupon_dto: CouponCreationDTO,
        db: AsyncSession = Depends(get_db)
):
    coupon_repository = SQLCouponRepository(db)
    coupon_service = CouponUseCases(coupon_repository)
    new_coupon = await coupon_service.add(coupon_dto)
    return new_coupon

@router.get("/", response_model=List[Coupon])
async def get_coupons(
        db: AsyncSession = Depends(get_db)
):
    coupon_repository = SQLCouponRepository(db)
    coupon_service = CouponUseCases(coupon_repository)
    coupons = await coupon_service.get_all()
    return coupons

@router.get("/{code}", response_model=Coupon)
async def get_coupon(code: str,
                   db: AsyncSession = Depends(get_db)
):
    coupon_repository = SQLCouponRepository(db)
    coupon_service = CouponUseCases(coupon_repository)
    coupon = await coupon_service.get_by_code(code)
    return coupon

@router.put("/{code}", response_model=dict)
async def coupon_update(updatecoupon_dto: CouponUpdateDTO,
                   db: AsyncSession = Depends(get_db)
):
    coupon_repository = SQLCouponRepository(db)
    coupon_service = CouponUseCases(coupon_repository)
    await coupon_service.update_coupon(updatecoupon_dto)
    return {"message": "Coupon updated successfully"}

@router.delete("/{code}", response_model=dict)
async def remove_coupon(code: str,
                   db: AsyncSession = Depends(get_db)
):
    coupon_repository = SQLCouponRepository(db)
    coupon_service = CouponUseCases(coupon_repository)
    await coupon_service.delete_coupon(code)
    return {"message": "Coupon deleted successfully"}