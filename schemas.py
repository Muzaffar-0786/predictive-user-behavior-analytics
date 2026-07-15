from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime


# -------------------------
# Authentication
# -------------------------

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


# -------------------------
# User
# -------------------------

class UserBase(BaseModel):
    full_name: str
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# -------------------------
# Video
# -------------------------

class VideoBase(BaseModel):
    title: str
    description: Optional[str] = None
    video_url: str
    thumbnail_url: Optional[str] = None
    category: Optional[str] = None


class VideoCreate(VideoBase):
    pass


class VideoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    category: Optional[str] = None


class VideoResponse(VideoBase):
    id: int
    views: int
    likes: int
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# -------------------------
# Watch History
# -------------------------

class WatchHistoryCreate(BaseModel):
    video_id: int


class WatchHistoryResponse(BaseModel):
    id: int
    user_id: int
    video_id: int
    watched_at: datetime

    model_config = ConfigDict(from_attributes=True)
