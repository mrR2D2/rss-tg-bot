"""
Module which contains common API router.
"""

import fastapi

from rss_reader.config import settings
from rss_reader.api.endpoints import category
from rss_reader.api.endpoints import post
from rss_reader.api.endpoints import rss_feed


api_router = fastapi.APIRouter(prefix=settings.API_V1_STR)
api_router.include_router(category.router)
api_router.include_router(post.router)
api_router.include_router(rss_feed.router)
