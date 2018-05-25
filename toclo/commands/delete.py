from .base import Base

class Delete(Base):
    def run(self):
        if self.options['<id>'] == "all":
            self.drop_table(self.table_name)
            self.drop_table(self.category_name)
        else:
            self.delete()