import os
import shutil
import logging
import tempfile
import unittest
import subprocess

try:
    from StringIO import StringIO # Python 2
except ImportError:
    from io import StringIO # Python 3

import script123

class TestModule(unittest.TestCase):
    """ Tests for scrip123.py """

    def test_install(self):
        """ Successfully installs package """
        self.tempdir = tempfile.mkdtemp()
        subprocess.check_call(["virtualenv", self.tempdir])
        subprocess.check_call([os.path.join(self.tempdir, "bin", "python"), "setup.py", "install"])
        subprocess.check_call([os.path.join(self.tempdir, "bin", "script123"), "-h"])
        shutil.rmtree(self.tempdir)

    def test_runs(self):
        """ Successfully issue a certificate via subject alt name """
        log_output = StringIO()
        debug_handler = logging.StreamHandler(log_output)
        script123.LOGGER.addHandler(debug_handler)
        script123.main([])
        log_output.seek(0)
        logged_messages = log_output.read().encode("utf8")
        self.assertIn("Hello World!", logged_messages.decode("utf8"))
        script123.LOGGER.removeHandler(debug_handler)

