"""CreateBooksTable Migration."""

from masoniteorm.migrations import Migration


class CreateBooksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("books") as table:
            table.increments("id")
            table.string("title", 100)
            table.string("author", 100)
            table.decimal("price", 17, 2)
            table.text("description")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("books")
