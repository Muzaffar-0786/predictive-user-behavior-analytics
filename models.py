from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, index=True, nullable=False)

    username = Column(String(50), unique=True, index=True, nullable=False)

    hashed_password = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True)

    is_admin = Column(Boolean, default=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    videos = relationship(
        "Video",
        back_populates="owner",
        cascade="all, delete",
    )

    watch_history = relationship(
        "WatchHistory",
        back_populates="user",
        cascade="all, delete",
    )


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    description = Column(Text)

    video_url = Column(String(500), nullable=False)

    thumbnail_url = Column(String(500))

    category = Column(String(100))

    views = Column(Integer, default=0)

    likes = Column(Integer, default=0)

    owner_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    owner = relationship(
        "User",
        back_populates="videos",
    )

    history = relationship(
        "WatchHistory",
        back_populates="video",
        cascade="all, delete",
    )


class WatchHistory(Base):
    __tablename__ = "watch_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
    )

    video_id = Column(
        Integer,
        ForeignKey("videos.id", ondelete="CASCADE"),
    )

    watched_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    user = relationship(
        "User",
        back_populates="watch_history",
    )

    video = relationship(
        "Video",
        back_populates="history",
    )
