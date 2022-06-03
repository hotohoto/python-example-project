"""custom math operations"""
import logging

import example.module2

_LOGGER = logging.getLogger(__name__)


def mean(list_like_obj):
    """Returns mean"""
    _LOGGER.debug("mean() %s", list_like_obj)

    example.module2.check_something()

    return total(list_like_obj) / len(list_like_obj)


def total(list_like_obj):
    """Returns sum"""
    _LOGGER.debug("total() %s", list_like_obj)

    current_sum = 0
    for _, val in enumerate(list_like_obj):
        current_sum += val
    return current_sum
