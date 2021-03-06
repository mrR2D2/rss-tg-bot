"""
Module which contains RSS Feed CRUD operations.
"""

from rss_reader.api import schemas
from rss_reader.api.crud import base
from rss_reader import models


class CrudRssFeed(
    base.CrudBase[models.RssFeed, schemas.RssFeedCreate, schemas.RssFeedUpdate],
):
    """
    RSS Feed CRUD class.
    """


rss_feed = CrudRssFeed(models.RssFeed)
