from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType



class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    isActive = Column(Boolean, default=True)
    isStaff = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', isActive={self.isActive}, isStaff={self.isStaff})>"





class Order(Base):
    ORDER_STATUS=(('PENDING', 'pending'), ('IN_TRANSITE', 'in_transite'), ('DELIVERED', 'delivered'))

    PIZZA_SIZE=(('SMALL', 'small'), ('MEDIUM', 'medium'), ('LARGE', 'large'), ('EXTRA_LARGE', 'extra_large'))
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    quantity = Column(String, unique=True, nullable=False)
    order_status = Column(ChoiceType(ORDER_STATUS), default='PENDING', nullable=False)
    pizza_size = Column(ChoiceType(PIZZA_SIZE), default='SMALL', nullable=False)
    flavour = Column(String, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    users = relationship('User', back_populates='orders')

    def __repr__(self):
        return f"<Order(quantity='{self.quantity}', order_status='{self.order_status}', pizza_size='{self.pizza_size}', flavor='{self.flavor}', user_id={self.user_id})>"