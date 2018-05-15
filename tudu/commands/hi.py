"""The hi command."""

from json import dump
from .base import Base


class Hi(Base):
    """Say hello, world!"""

    def run(self):
        print('HIHIIHIHIHI')
        # print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
