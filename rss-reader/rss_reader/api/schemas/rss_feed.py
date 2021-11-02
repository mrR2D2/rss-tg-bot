"""
Module which contains API schema definition for RSS Feeds.
"""

from datetime import datetime
from typing import Optional

import pydantic
from pydantic.networks import HttpUrl

from rss_reader.api.schemas import category as category_schemas


class RssFeedCreate(pydantic.BaseModel):
    """
    Model used for RSS feed creation.
    """
    name: str
    url: HttpUrl


class RssFeedUpdate(pydantic.BaseModel):
    """
    Model used for RSS feed update.
    """
    name: Optional[str] = None
    url: Optional[HttpUrl] = None


class RssFeed(pydantic.BaseModel):
    """
    Model used for RSS feed representation.
    """
    id: int

    name: str
    url: HttpUrl
    category: Optional[category_schemas.Category] = None

    parsed_at: Optional[datetime]
    modified_at: Optional[datetime]
    etag: Optional[str]

    created_at: datetime

    class Config:
        orm_mode = True