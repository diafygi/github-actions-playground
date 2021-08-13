import logging
import unittest

try:
    from StringIO import StringIO # Python 2
except ImportError:
    from io import StringIO # Python 3

import script123

class TestModule(unittest.TestCase):
    """ Tests for scrip123.py """

    def test_success_domain(self):
        """ Successfully issue a certificate via subject alt name """

        # capture logged stderr output
        log_output = StringIO()
        debug_handler = logging.StreamHandler(log_output)
        script123.LOGGER.addHandler(debug_handler)

        # run the module's script
        script123.run123()

        # make sure logged output is correct
        log_output.seek(0)
        logged_messages = log_output.read().encode("utf8")
        self.assertIn("Hello World!", logged_messages.decode("utf8"))

        # revert logging capture
        script123.LOGGER.removeHandler(debug_handler)

