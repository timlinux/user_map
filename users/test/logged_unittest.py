# -*- coding: utf-8 -*-
"""
    Provides a custom unit test base class which will log to sentry.

    :copyright: (c) 2010 by Tim Sutton
    :license: GPLv3, see LICENSE for more details.
"""
import unittest
import logging
from users import setup_logger

setup_logger()
LOGGER = logging.getLogger('user_map')


class LoggedTestCase(unittest.TestCase):
    """A test class that logs to sentry on failure."""
    def failure_exception(self, msg):
        """Overloaded failure exception that will log to sentry.

        :param msg: str - a string containing a message for the log entry.

        Delegates to TestCase and returns the exception generated by it.

        see unittest.TestCase

        """
        LOGGER.exception(msg)

        #pylint: disable=E1101
        #noinspection PyUnresolvedReferences
        return self.super(LoggedTestCase, self).failure_exception(msg)
        #pylint: enable=E1101
