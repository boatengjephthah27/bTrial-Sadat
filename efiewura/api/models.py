# from .database import Base
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# from sqlalchemy_imageattach.entity import Image, image_attachment


class ProfileImages(Base):
    __tablename__ = "profile_images"

    id = Column(Integer, primary_key=True, index=True)
    image = Column()
    image_path = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="profile")


class CompanyLogos(Base):
    __tablename__ = "company_logos"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="company_logo")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    is_active = Column(Boolean)
    user_type = Column(String)
    company_name = Column(String)
    phone = Column(String)
    company_logo = relationship("CompanyLogos", back_populates="user")
    profile = relationship("ProfileImages", back_populates="user")
