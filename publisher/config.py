# Global site configuration settings.

SITE_CONFIG = {
    'SITE_NAME': 'Crimson Publisher',
    'SITE_DESCRIPTION': 'Crimson Publisher Open Source Project.',
    'ARTICLE_NAME': 'Article',
    'ARTICLE_NAME_PLURAL': 'Articles',
    'BOOK_NAME': 'Book',
    'BOOK_NAME_PLURAL': 'Books',
    'ALLOW_COMMENTS': True,
    'MODERATE_COMMENTS': True,
    'SHOW_ARTICLES': True,
    'SHOW_BOOKS': True,
}


try:
    from publisher.custom_config import *
except ImportError:
    pass
