from .base import Base  # noqa
from .category import Category  # noqa
from .post import Post  # noqa
from .rss_feed import RssFeed  # noqa
from .user import User   # noqa


all_models = [
    Category,
    Post,
    RssFeed,
    User,
]
