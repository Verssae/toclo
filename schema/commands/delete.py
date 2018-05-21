from .base import Base

class Delete(Base):
    def run(self):
        self.delete()