
from .base import Base

class Ls(Base):
    """Show List"""

    def run(self):
        if self.options['<ctgr>'] == "done":
            self.show(None, 1)
        elif self.options['<ctgr>'] == "all":
            self.show(None, None)
        else:
            self.show(self.options['<ctgr>'],1 if self.options['<done>'] == "done" else 0)
        

