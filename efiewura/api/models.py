from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy.sql import func

# from sqlalchemy_imageattach.entity import Image, image_attachment


# Profile Images Model ....................................................................................................
class ProfileImages(Base):
    __tablename__ = "profile_images"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="profile")


# Company Logos Model ....................................................................................................
class CompanyLogos(Base):
    __tablename__ = "company_logos"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="company_logo")


# Users Model ....................................................................................................
class User(Base):
    """
    Users

    Args:
        Base (_type_): _description_
    """

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
    date = Column(DateTime(timezone=True), default=func.now())

    company_logo = relationship("CompanyLogos", back_populates="user")
    profile = relationship("ProfileImages", back_populates="user")
    favourites = relationship("Favourites", back_populates="user")
    application = relationship("Application", back_populates="user")
    property = relationship("Property", back_populates="host")
    review = relationship("Review", back_populates="user")


# Property Images Model ....................................................................................................
class PropertyImages(Base):
    __tablename__ = "property_images"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    property_id = Column(Integer, ForeignKey('properties.id'))

    property = relationship("Property", back_populates="propertyimages")


# Properties Model ....................................................................................................
class Property(Base):
    """Properties

    Args:
        Base (_type_): _description_
    """

    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    building_type = Column(String)
    featured = Column(Boolean)
    sale_type = Column(String)
    location = Column(String)
    hosted = Column(Integer, ForeignKey('users.id'))
    availability = Column(Boolean)
    months = Column(Integer)
    landsize = Column(Integer)
    price = Column(Integer)
    bedroom = Column(Integer)
    bathroom = Column(Integer)
    latitude = Column(String)
    longitude = Column(String)
    description = Column(String)
    date = Column(DateTime(timezone=True), default=func.now())

    propertyimages = relationship("PropertyImages", back_populates="property")
    favourites = relationship("Favourites", back_populates="property")
    host = relationship("User", back_populates="property")
    application = relationship("Application", back_populates="property")
    review = relationship("Review", back_populates="property")
    amenity = relationship("Amenity", back_populates="property")
    otheramenity = relationship("OtherAmenity", back_populates="property")


# Blogs Model ....................................................................................................
class Blog(Base):
    """Blogs

    Args:
        Base (_type_): _description_
    """

    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    image = Column(String)
    video = Column(String)
    date = Column(DateTime(timezone=True), default=func.now())


# Sponsors Model ....................................................................................................
class Sponsors(Base):
    """Sponsors

    Args:
        Base (_type_): _description_
    """

    __tablename__ = 'sponsors'

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    company_logo = Column(String)


# Favourites Model ....................................................................................................
class Favourites(Base):
    """Favourites

    Args:
        Base (_type_): _description_
    """

    __tablename__ = 'favourites'

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime(timezone=True), default=func.now())

    user = relationship("User", back_populates="favourites")
    property = relationship("Property", back_populates="favourites")


# Application Model ....................................................................................................
class Application(Base):
    """Application

    Args:
        Base (_type_): _description_
    """

    __tablename__ = 'application'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String)
    phone = Column(String)
    occupation = Column(String)
    current_location = Column(String)
    preferred_language = Column(String)
    ownership_status = Column(String)
    sell_before_purchase = Column(String)
    help_relocating = Column(String)
    contact_preference = Column(String)
    contact_time = Column(String)
    purchase_offer = Column(Integer)
    household_number = Column(String)
    married = Column(Boolean)
    spouse_name = Column(String)
    spouse_email = Column(String)
    spouse_phone = Column(String)
    contact_spouse = Column(Boolean)
    monthly_income = Column(Integer)
    comment = Column(String)
    date = Column(DateTime(timezone=True), default=func.now())
    property_id = Column(Integer, ForeignKey('properties.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="application")
    property = relationship("Property", back_populates="application")


# Application Details Model ....................................................................................................
# class ApplicationDetails(Base):
#     """Application Details

#     Args:
#         Base (_type_): _description_
#     """

#     __tablename__ = 'application_details'

#     id = Column(Integer, primary_key=True, index=True)
#     full_name = Column(String)
#     email = Column(String)
#     phone = Column(String)
#     occupation = Column(String)
#     current_location = Column(String)
#     preferred_language = Column(String)
#     ownership_status = Column(String)
#     sell_before_purchase = Column(String)
#     help_relocating = Column(String)
#     contact_preference = Column(String)
#     contact_time = Column(String)
#     purchase_offer = Column(Integer)
#     household_number = Column(String)
#     married = Column(Boolean)
#     spouse_name = Column(String)
#     spouse_email = Column(String)
#     spouse_phone = Column(String)
#     contact_spouse = Column(Boolean)
#     monthly_income = Column(Integer)
#     comment = Column(String)


# Reviews Model ....................................................................................................

class Review(Base):

    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    review = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    property_id = Column(Integer, ForeignKey('properties.id'))
    date = Column(DateTime(timezone=True), default=func.now())

    user = relationship("User", back_populates="review")
    property = relationship("Property", back_populates="review")


# Amenities Model ....................................................................................................

class Amenity(Base):

    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    property_id = Column(Integer, ForeignKey('properties.id'))

    property = relationship("Property", back_populates="amenity")


# OtherAmenities Model ....................................................................................................

class OtherAmenity(Base):

    __tablename__ = 'otheramenities'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    property_id = Column(Integer, ForeignKey('properties.id'))

    property = relationship("Property", back_populates="otheramenity")
