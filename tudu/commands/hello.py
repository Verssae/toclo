"""The hello command."""


from json import dumps

from .base import Base


class Hello(Base):
    """Say hello, world!"""

    def run(self):
        s = input("plz enter : ")
        print(s)
        # print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
