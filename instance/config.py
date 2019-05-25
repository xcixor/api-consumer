"""Contains api configurations."""

import os


class Config:
    """Basic settings for all configurations."""

    PROPAGATE_EXCEPTIONS = True


class Development(Config):
    """Development configurations."""

    DEBUG = True


# Register the configurations
CONFIG = {
    'development': Development,
    'default': Development
}