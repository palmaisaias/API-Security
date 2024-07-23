from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class Customer(Base):
    __tablename__ = 'Customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_name: Mapped[str] = mapped_column(db.String(200), nullable=False)
    email: Mapped[str] = mapped_column(db.String(200), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=False)
    username: Mapped[str] = mapped_column(db.String(200), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(200), nullable=False)
    role_id: Mapped[int] = mapped_column(db.ForeignKey('Roles.id'))

    role: Mapped['Role'] = db.relationship('Role', back_populates='customers')
    orders: Mapped[List["Order"]] = db.relationship('Order', back_populates="customer")
