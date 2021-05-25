"""module 2"""

import logging

_LOGGER = logging.getLogger(__name__)


def check_something():
    """checks something"""

    _LOGGER.debug("Checking something...")
    _LOGGER.info("Checking something...")
    _LOGGER.warning("Checking something...")
