from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ARRAY, DECIMAL
from sqlalchemy.ext.mutable import MutableList

from domain.models.coupon import Coupon
from infrastructure.db.base_class import Base


class CouponOrmModel(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    code = Column(String(20), default=None)
    type = Column(String(10), nullable=False)  # 'absolute'/'percentage'
    discount = Column(DECIMAL(15, 4), nullable=False)
    logged = Column(Boolean)
    total = Column(DECIMAL(15, 4), nullable=False)
    date_start = Column(Date, nullable=False)
    date_end = Column(Date, nullable=False)
    uses_total = Column(Integer, nullable=False)
    uses_customer = Column(String(11), nullable=False)
    active = Column(Boolean, nullable=False)  # Status changed to 'active'
    date_added = Column(DateTime, nullable=False)
    skus = Column(ARRAY(Integer))
    collections = Column(ARRAY(Integer))

    @staticmethod
    def from_domain(coupon: Coupon):
        """Create a CouponOrmModel instance from a Coupon domain model."""
        return CouponOrmModel(
            id=coupon.id,
            name=coupon.name,
            code=coupon.code,
            type=coupon.type,
            discount=coupon.discount,
            logged=coupon.logged,
            total=coupon.total,
            date_start=coupon.date_start,
            date_end=coupon.date_end,
            uses_total=coupon.uses_total,
            uses_customer=coupon.uses_customer,
            active=coupon.status,  # Assuming domain status is named 'status'
            date_added=coupon.date_added,
            skus=coupon.skus,
            collections=coupon.collections
        )

    def to_domain(self) -> Coupon:
        """Convert this CouponOrmModel instance to a Coupon domain model."""
        return Coupon(
            id=self.id,
            name=self.name,
            code=self.code,
            type=self.type,
            discount=self.discount,
            logged=self.logged,
            total=self.total,
            date_start=self.date_start,
            date_end=self.date_end,
            uses_total=self.uses_total,
            uses_customer=self.uses_customer,
            status=self.active,  # Assuming domain status is named 'status'
            date_added=self.date_added,
            skus=self.skus,
            collections=self.collections
        )

