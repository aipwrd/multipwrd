"""\
MultiPWRD Custom Exceptions
===========================

Author: XA <xa@mes3.dev> from <AI PWRD Development Team>
Created on: Wednesday, July 03, 2023
Last updated on: Wednesday, July 03, 2023

This module defines custom exception classes for the MultiPWRD framework.
These exceptions are used throughout the MultiPWRD framework to handle
various error conditions in a consistent and meaningful way.
"""

from __future__ import annotations


class MultiPWRDException(Exception):
    """Base class for all exceptions raised by MultiPWRD framework."""

    pass


class ConfigurationError(MultiPWRDException):
    """MultiPWRD's configuration is incorrectly set."""

    pass
