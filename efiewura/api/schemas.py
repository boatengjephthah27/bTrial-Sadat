from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from fastapi import File, UploadFile
from enum import Enum
import uuid


class Color(str, Enum):
    normalUser = "N"
    partner = "P"
    superUser = "S"


# class ImageCreate(BaseModel):
#     image: UploadFile


# class LogoImage(ImageCreate):
#     user_id: int


# class ProfileImage(ImageCreate):
#     user_id: int


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
    email: str
    first_name: str
    last_name: str
    password: str
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
    company_logo: List[ShowLogoImage] = []
    profile: List[ShowProfileImage] = []

    class Config():
        orm_mode = True
