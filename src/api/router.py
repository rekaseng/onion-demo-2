from fastapi import APIRouter

from api.endpoints import user_endpoint, coupon_endpoint

api_router = APIRouter()

api_router.include_router(user_endpoint.router, prefix="/users", tags=["Users"])
api_router.include_router(coupon_endpoint.router, prefix="/coupons", tags=["Coupons"])

