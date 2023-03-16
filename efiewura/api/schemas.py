from pydantic import BaseModel, Field
from pydantic.types import SecretStr
from pydantic.networks import EmailStr
from typing import List, Optional, Dict
from fastapi import File, UploadFile, Form
from enum import Enum
from datetime import datetime


# User Schema ....................................................................................................

class Color(str, Enum):
    normalUser = "N"
    partner = "P"
    superUser = "S"


class ImageCreate(BaseModel):
    img: UploadFile


class LogoImage(ImageCreate):
    image: str
    user_id: int


class ProfileImage(ImageCreate):
    user_id: int


class ShowLogoImage(BaseModel):
    image: str
    id: int
    user_id: int

    class Config:
        orm_mode = True


class ShowProfileImage(BaseModel):
    image: str
    id: int
    user_id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    email: Optional[EmailStr] = Field(unique=True)
    first_name: str
    last_name: str
    password: Optional[SecretStr]
    is_active: bool
    user_type: Color
    company_name: Optional[str]
    phone: Optional[str]


class ShowUser(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    password: str
    is_active: bool
    user_type: Color
    company_name: Optional[str]
    phone: Optional[str]
    date: datetime = None
    company_logo: List[ShowLogoImage] = []
    profile: List[ShowProfileImage] = []

    class Config():
        orm_mode = True


# Property Schema ....................................................................................................

class BuildingType(str, Enum):
    home = "H"
    apartment_flat = "AF"
    office = "O"
    self_contain = "SC"
    storey_building = "SB"
    retail = "R"
    industrial = "I"


class SaleType(str, Enum):
    rent = "R"
    sale = "S"


class PropertyImage(BaseModel):
    image: str
    user_id: int


class Review(BaseModel):
    review: str
    user_id: int
    property_id: int


class Amenity(BaseModel):
    type: str
    property_id: int


class OtherAmenity(BaseModel):
    type: str
    property_id: int


class ShowPropertyImage(BaseModel):
    image: str
    id: int
    user_id: int

    class Config:
        orm_mode = True


class ShowOtherAmenity(BaseModel):
    id: int
    type: str
    property_id: int

    class Config:
        orm_mode = True


class ShowAmenity(BaseModel):
    id: int
    type: str
    property_id: int

    class Config:
        orm_mode = True


class ShowReview(BaseModel):
    id: int
    review: str
    date: datetime = None
    user_id: int
    property_id: int

    class Config:
        orm_mode = True


class Property(BaseModel):
    name: str
    building_type: BuildingType
    featured: bool
    sale_type: SaleType
    location: str
    hosted: int
    availability: bool
    months: int
    landsize: int
    price: int
    bedroom: int
    bathroom: int
    latitude: str
    longitude: str
    description: str


class ShowProperty(BaseModel):
    name: str
    building_type: BuildingType
    featured: bool
    sale_type: SaleType
    location: str
    hosted: List[ShowUser] = []
    availability: bool
    months: int
    landsize: int
    price: int
    bedroom: int
    bathroom: int
    latitude: str
    longitude: str
    description: str
    date: datetime = None
    propertyimages: List[ShowPropertyImage] = []
    amenities: List[ShowAmenity] = []
    otheramenities: List[ShowOtherAmenity] = []
    # reviews : List[] = []

    class Config:
        orm_mode = True
