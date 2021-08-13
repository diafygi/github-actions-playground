import sys
import logging
import argparse

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.INFO)

def run123():
    LOGGER.info("Hello World!")

def main(argv=None):
    parser = argparse.ArgumentParser()
    args = parser.parse_args(argv)
    run123()

if __name__ == "__main__": # pragma: no cover
    main(sys.argv[1:])

