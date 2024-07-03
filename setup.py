"""\
MultiPWRD
=========

Author: XA <xa@mes3.dev> from <AI PWRD Development Team>
Created on: Wednesday, July 03, 2023
Last updated on: Wednesday, July 03, 2023
"""

import platform
import site
import sys

from pkg_resources import parse_version

try:
    import setuptools
except ImportError:
    raise RuntimeError(
        "Could not install MultiPWRD in the environment as setuptools is "
        "missing. Please create a new virtual environment before proceeding."
    )

mini_py_version: str = "3.10"
pwrd_py_version: str = platform.python_version()

if parse_version(pwrd_py_version) < parse_version(mini_py_version):
    raise SystemExit(
        "Could not install MultiPWRD! It requires python version 3.10+, "
        f"you are using {pwrd_py_version}..."
    )

# BUG: Cannot install into user directory with editable source.
# Using this solution: https://stackoverflow.com/a/68487739/14316408
# to solve the problem with installation. As of October, 2022 the issue
# is still open on GitHub: https://github.com/pypa/pip/issues/7953.
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

if __name__ == "__main__":
    setuptools.setup()
